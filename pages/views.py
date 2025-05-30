from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from listings.models import Listing

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {"listings": listings}
    return render(request,'pages/index.html', context)

def about(request):
    pages_url = reverse('pages:about')
    return render(request,'pages/about.html')