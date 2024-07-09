# studentApp/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True}),
        error_messages={'required': 'Username is required.'},
    )
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput,
        error_messages={'required': 'Password is required.'},
    )

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                "This account is inactive.",
                code='inactive',
            )
