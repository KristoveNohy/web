from django import forms
from .models import Customer

class ContactForm(forms.ModelForm):
    attachment = forms.FileField(required=False)

    class Meta:
        model = Customer
        fields = "__all__"

    
