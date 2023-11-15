from django import forms
from item.models import *
from center.models import *


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, label="Ваше  ФИО", widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=255,  widget=forms.EmailInput(attrs={'class':'form-control'}))
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), label="Интересующий специалист", widget=forms.Select(attrs={'class':'form-select'}))