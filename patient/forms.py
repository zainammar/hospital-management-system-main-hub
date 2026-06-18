from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = [
            'user',
            'created_at',
            'updated_at',
        ]