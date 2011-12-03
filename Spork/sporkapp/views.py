from django.template import Context, loader
from django.shortcuts import render_to_response
from django.http import HttpResponse

from sporkapp.models import Donation
from sporkapp.forms import NewDonationForm

# Create your views here.
def home(request):
    return render_to_response('home.html')
   # return HttpResponse(loader.get_template('home.html'))

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
        return render_to_response('create_donation.html', {'form' : form})
