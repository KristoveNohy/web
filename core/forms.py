from django import forms
from .models import Customer

class ContactForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
    
    attachment = forms.FileField(required=False,)
    
