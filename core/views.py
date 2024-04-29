from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Bike
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
import subprocess
import requests
import time
from django.http import JsonResponse


def home(request):
    return render(request, 'homepage.html')

def login_view(request):
    print("Inside login_view function")  # Add this line for debugging
    # Logic for handling login
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print("Form is valid")  # Add this line for debugging
            user = form.get_user()
            auth_login(request, user)
            print("User authenticated:", user)  # Add this line for debugging
            print("Redirecting to bike_inventory")  # Add this line for debugging
            return redirect('bike_inventory')  # Redirect to the bike inventory page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_user = authenticate(username=user.username, password=request.POST['password1'])
            if auth_user:
                auth_login(request, auth_user)
                return redirect('bike_inventory')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def bike_inventory(request):
    bikes = Bike.objects.filter(available=True)
    return render(request, 'bike_inventory.html', {'bikes': bikes})


@login_required
def process_rental_request(request):
    # Run Flask app
    flask_process = subprocess.Popen(['python', 'flask_app.py'])
    # Run Bottle app
    bottle_process = subprocess.Popen(['python', 'bottle_app.py'])
    
    # Wait for apps to start
    time.sleep(2)
    
    # Make requests to Flask app
    flask_response = requests.post('http://localhost:5000/rental', json={'data': 'rental_data'})
    flask_message = flask_response.json()  # Handle response from Flask app
    
    # Make requests to Bottle app
    bottle_response = requests.get('http://localhost:8080/interaction')
    bottle_message = bottle_response.text  # Handle response from Bottle app
    
    # Close Flask and Bottle processes
    flask_process.terminate()
    bottle_process.terminate()
    
    # Process responses and return appropriate response to the client
    return JsonResponse({'flask_response': flask_message, 'bottle_response': bottle_message})
