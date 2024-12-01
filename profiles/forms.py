from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile
from django.contrib.auth.forms import AuthenticationForm

# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = Profile
#         fields = ['username', 'email', 'password1', 'password2']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Поле email, обязательное для заполнения
    username = forms.CharField(max_length=50, help_text='Максимум 50 символов')
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'}),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
    )

