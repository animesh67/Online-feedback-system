from django import forms
from django.forms import ModelForm
from django.db import models
from .models import Student
from .models import Teacher


class StudentRegister(forms.Form):
    name = forms.CharField(label='Your name')
    sid= forms.IntegerField(label='Your Sid', required= True)
    password = forms.CharField(label='your password')
    branch = forms.CharField(label='your branch')
    email_id = forms.CharField(label='Your email id')
    address = forms.CharField(label='your address')


class StudentLogin(forms.Form):
    sid=forms.IntegerField(label='Your sid')
    password=forms.CharField(label='Your Password')
