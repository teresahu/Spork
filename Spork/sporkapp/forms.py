from django import forms

from sporkapp.models import Donation

class SubscribeForm(forms.Form):
    email = forms.EmailField(required=True)
    firstname = forms.CharField(max_length = 30)
    lastname = forms.CharField(max_length = 30)

class NewDonationForm(forms.ModelForm):
    class Meta:
        model = Donation

