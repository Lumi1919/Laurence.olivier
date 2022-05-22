from django.forms import ModelForm
from django.forms import ModelForm, TextInput, TextInput, EmailField
from django import forms
from .models import ReservationsSeance


class ReservationsSeanceForm(forms.ModelForm):
    class Meta:
        model = ReservationsSeance
        fields = ['nom', 'mail', 'Jour', 'HeureDebut', 'HeureFin']

        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'mail': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'Jour': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'Date'}),
            'HeureDebut': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'HeureFin': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }
