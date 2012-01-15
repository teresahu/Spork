from django import forms

from sporkapp.models import Donation

class SubscribeForm(forms.Form):
    email_address = forms.EmailField(required=True)
    firstname = forms.CharField(max_length = 30, required=False)
    lastname = forms.CharField(max_length = 30, required=False)

class NewDonationForm(forms.ModelForm):
    class Meta:
        model = Donation

