from django.shortcuts import render, redirect
import uuid
from .models import ShortURL
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
            original_url = request.POST['link']
            short_url = str(uuid.uuid4())[:5]
            new_url = ShortURL(original_url=original_url, short_url=short_url)
            new_url.save()
            return HttpResponse(short_url)
    

def go(request, pk):    
    short_url = ShortURL.objects.get(short_url=pk)
    return redirect(short_url.original_url)