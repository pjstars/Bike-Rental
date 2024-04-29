from django.shortcuts import render
from django.http import HttpResponse

def inventory_view(request):
    # Handle inventory logic here
    return HttpResponse("This is the bike inventory page.")
