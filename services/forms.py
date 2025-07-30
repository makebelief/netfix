from django import forms
from .models import RequestService

class RequestServiceForm(forms.ModelForm):
    class Meta:
        model = RequestService
        fields = ['requested_date', 'notes']
        widgets = {
            'requested_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'notes': forms.Textarea(attrs={'rows': 4}),
        }
