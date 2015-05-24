from django.shortcuts import render
from django.http import HttpResponse
import os
import subprocess

################################################################################
def see_songs(request):
    return render(request, 'addsong/see_songs.html', {})

def handle_request(request):
	return render(request, 'handle_request/handle.html')

def search(request):
    if 'q' in request.POST:
    	#print request.POST['q']
    	arg1 = request.POST['q']
    	os.system('python /home/James/Desktop/WHPUK/hwpuk/addsong/add_songs.py %s' %(arg1))
    	#subprocess.Popen('/home/James/Desktop/WHPUK/hwpuk/add_songs.py')
        message = 'You searched for: %r' % request.POST['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
