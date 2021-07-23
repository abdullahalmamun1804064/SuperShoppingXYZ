from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,AuthenticationForm, UsernameField,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from django.forms import widgets
from django.utils.translation import ugettext_lazy as _
from .models import Customer,Product,Cart,Orderplaced


#registration
class userregistation(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(label='Email',required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
   # username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']

        widgets= {
            'username':forms.TextInput(attrs={'class':'form-control'}),
        }
#loging pass

class login_form(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'class':'form-control','autofocus':True}))
    password= forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'current-password'}))

#password change

class MypasswordchangeForm(PasswordChangeForm):
    old_password=forms.CharField(label=_('Old Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password1=forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2=forms.CharField(label='Confirm New Password',widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))

#password forget

class MyPasswordResetForm(PasswordResetForm):
    email=forms.EmailField(label=_('Email'),max_length=254,widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1=forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2=forms.CharField(label='Confirm New Password',widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))

#customar
class profile_From(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','locality','city','zipcode','state']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control','placeholder':'1234 Main st'}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':'Apartment,studio,of floor'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'zipcode':forms.NumberInput(attrs={'class':'form-control'}),



        }