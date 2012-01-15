import json
import urllib

from django.template import Context, loader
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from sporkapp.models import Donation
from sporkapp.forms import NewDonationForm, SubscribeForm

# Create your views here.
def subscribe(request):
    MAILCHIMP_API_KEY = ''
    MAILCHIMP_API_ENDPOINT_URL = 'http://us4.api.mailchimp.com/1.3/?method=listSubscribe'
    MAILCHIMP_LIST_ID = ''
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            api_params = {
                'apikey': MAILCHIMP_API_KEY,
                'id' : MAILCHIMP_LIST_ID,
                'email_address' : form.cleaned_data['email_address']
            }
            result = urllib.urlopen(MAILCHIMP_API_ENDPOINT_URL, json.dumps(api_params))
            result_json = json.loads(result.readlines())
            if result_json == True:
                return render_to_response('subscribe_thanks.html', context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect('/home/')
    else:
        subscribe_form = SubscribeForm()
        return render_to_response('subscribe.html', {'subscribe_form' : subscribe_form}, context_instance=RequestContext(request))

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
