from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirme a Senha')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'Nome de Usuário',
            'email': 'Email',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('As senhas não coincidem.')

class LoginForm(forms.Form):
    username = forms.CharField(label='Nome de Usuário')
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')