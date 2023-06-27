from django import forms

class ContactForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField(required=True)
    subject=forms.CharField(required=True)
    message=forms.CharField(qidget=forms.Textarea,required=True)