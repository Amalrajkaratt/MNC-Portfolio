from django import forms
from .models import ServiceSigup,CareerSignup

# SIGNUPFORM for clients
class ServiceSignUpForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=6)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=6)
    class Meta():
        model=ServiceSigup
        fields='__all__'

# Login form for clients( service page login )
class ServiceLogInForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8)
    class Meta():
        model=ServiceSigup
        fields=('ContactEmail','Password')

# Career signup page
class CSignupForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=6)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=6)
    class Meta():
        model=CareerSignup
        fields='__all__'

# Login form for job seekers( career page login )
class CareerLogInForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8)
    class Meta():
        model=CareerSignup
        fields=('Email','Password')

# changepassword for career
class ChangePassword(forms.Form):
    OldPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=6)
    NewPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=6)
    ConfirmNewPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=6)

# Update for career
class CUpdateForm(forms.ModelForm):
    class Meta():
        model=CareerSignup
        fields=('Name','Email','ContactNumber',)