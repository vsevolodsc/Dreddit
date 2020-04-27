from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from difflib import SequenceMatcher
from django.conf import settings
from django.core.exceptions import ValidationError



class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class NumericPasswordValidator:
    """
    Validate whether the password is alphanumeric.
    """
    def validate(self, password, user=None):
        SpecialSym = ['$', '@', '#', '%', '!', '-', '_', '+', '*', '/']
        if password.isdigit():
            raise ValidationError(
                _("This password is entirely numeric."),
                code='password_entirely_numeric',
            )
        if not any(char.isupper() for char in password):
            raise ValidationError(
                _("This password does not contain any uppercase letters. "),
                code='password_no_upper',
            )
        if not any(char.islower() for char in password):
            raise ValidationError(
                _("This password does not contain any lower letters. "),
                code='password_no_lower',
            )

        if not any(char in SpecialSym for char in password):raise ValidationError(
                _("Password should have at least one of the symbols $@#%!-_+*/"),
                code='password_no_special',
            )

    def get_help_text(self):
        return _("Your password can't be entirely numeric.")