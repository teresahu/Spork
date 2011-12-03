from django.forms import ModelForm

from sporkapp.models import Donation

class NewDonationForm(ModelForm):
    class Meta:
        model = Donation


