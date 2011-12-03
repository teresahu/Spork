from django.template import Context, loader
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse(loader.get_template('home.html'))
