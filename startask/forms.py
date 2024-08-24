# myapp/forms.py
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import User
from django.contrib.auth import authenticate

# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']  

#     password = forms.CharField(widget=forms.PasswordInput)

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data['password']) 
#         if commit:
#             user.save()
#         return user


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-password-login'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-password-login'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-user-login'}),
            'email': forms.EmailInput(attrs={'class': 'form-user-login'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            self.add_error('password2', "As senhas não coincidem")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user




class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Usuário ou senha inválidos.")
            cleaned_data['user'] = user
        return cleaned_data



