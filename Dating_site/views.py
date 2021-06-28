from django.shortcuts import render

from django.shortcuts import render
from .models import Abilities, Prices, Clients

def index(request):
    site_Abilities = Abilities.objects.all()
    price = Prices.objects.all()
    client = Clients.objects.all()
    context = {
        'ability' : site_Abilities,
        'price' : price,
        'client' : client
    }
    return render(request, 'blog/index.html', context)

