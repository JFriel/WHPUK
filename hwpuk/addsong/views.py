from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def see_songs(request):
    return render(request, 'addsong/see_songs.html', {})

def handle_request(request):
	return render(request, 'handle_request/handle.html')

def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
