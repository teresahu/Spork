from django.template import Context, loader
from django.shortcuts import render_to_response
from django.http import HttpResponse

from sporkapp.models import Donation
from sporkapp.forms import NewDonationForm, SubscribeForm

# Create your views here.
def home(request):
    donations = Donation.objects.all()
    subscribe_form = SubscribeForm()
    return render_to_response('home.html', {'donations' : donations, 'subscribe_form' : subscribe_form})

def donation(request, donation_id):
    donation = Donation.objects.get(pk=donation_id)
    return render_to_response('donation_details.html', {'donation' : donation})

def create_donation(request):
    if(request.method) == 'POST':
        form = NewDonationForm(request.POST)
        if form.is_valid():
            return render_to_response('donation_thanks.html')
    else:
        form = NewDonationForm()
        return render_to_response('donate.html', {'form' : form})
