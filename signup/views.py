from django.shortcuts import render
from django.http import HttpResponse

def signup_view(request):
    # Handle signup logic here
    return HttpResponse("This is the signup page.")
