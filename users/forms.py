from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import password_validation, get_user_model
from django.utils.translation import gettext_lazy as _


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        min_length=3,
        max_length=255,
        required=True,
        help_text='Enter a unique valid email address for login.',
        widget=(
            forms.TextInput(attrs={'class': 'form-control', 'type': 'email'})
        )
    )
    first_name = forms.CharField(
        min_length=4,
        max_length=45,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        min_length=4,
        max_length=45,
        required=True,
        widget=(forms.TextInput(attrs={'class': 'form-control'}))
    )
    password1 = forms.CharField(
        min_length=8,
        label=_('Password'),
        widget=(forms.PasswordInput(attrs={'class': 'form-control'})),
        help_text=password_validation.password_validators_help_text_html()
    )
    password2 = forms.CharField(
        min_length=8,
        label=_('Password Confirmation'),
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=_('Enter the same password, for confirmation')
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        min_length=3,
        max_length=255,
        required=True,
        widget=(
            forms.TextInput(attrs={'class': 'form-control', 'type': 'email'})
        )
    )
    password = forms.CharField(
        min_length=8,
        required=True,
        widget=(forms.PasswordInput(attrs={'class': 'form-control'}))
    )
