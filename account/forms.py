from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import Custom_User

class UserRegistrationForm(UserCreationForm):
    USER_TYPE = (
        ('Job Seeker', 'Job Seeker'),
        ('Recruiter', 'Recruiter'),
    )
    
    display_name = forms.CharField(label='Display Name', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Display Name'}
    ))
    username = forms.CharField(label='Username', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Username'}
    ))
    email = forms.EmailField(label='Email Address', max_length=100, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}
    ))
    password1 = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'})
    )
    password2 = forms.CharField(label='Confirm Password', max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Confirm Password'}
    ))
    user_type = forms.CharField(label='User Type', required=True, max_length=20, widget=forms.Select(choices=USER_TYPE, attrs={'class': 'form-control'}))
    
    class Meta:
        model = Custom_User
        fields = ['display_name', 'username', 'email', 'user_type']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))




class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label='New Password', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='New Confirm Passowrd', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ForgetPassword(forms.Form):
    email = forms.EmailField(max_length=50, label='Email Address', widget=forms.EmailInput(attrs={'class': 'form-control'}))


class ResetPasswordForm(forms.Form):
    otp = forms.CharField(max_length=6, label='OTP', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label='New Password', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='New Confirm Passowrd', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    

class RegistrationVerificationForm(forms.Form):
    otp = forms.CharField(max_length=6, label='OTP', widget=forms.NumberInput(attrs={'class': 'form-control'}))



