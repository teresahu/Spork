# Create your views here.
def home(request):
    return HttpResponse(loader.get_template('home.html')
