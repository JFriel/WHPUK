from django.shortcuts import render

# Create your views here.
def see_songs(request):
    return render(request, 'addsong/see_songs.html', {})