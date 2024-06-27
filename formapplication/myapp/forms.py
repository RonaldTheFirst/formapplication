from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_no', 'customer_name', 'customer_surname', 'customer_dob', 'customer_occupation']
