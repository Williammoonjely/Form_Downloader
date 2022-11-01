from django import forms
from django.contrib.auth.models import User


class InfoForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'PlaceHolder':'First Name',
        'class':'form-control',
        'autofocus':'autofocus',
        'required':'required',}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'PlaceHolder':'Last Name',
        'class':'form-control',
        'required':'required',}))
    adhaar_number = forms.CharField(widget=forms.TextInput(attrs={
        'PlaceHolder':'Adhaar Number',
        'class':'form-control',
        'required':'required',}))
    account_number = forms.CharField(widget=forms.TextInput(attrs={
        'PlaceHolder':'Account Number',
        'class':'form-control',
        'required':'required',}))