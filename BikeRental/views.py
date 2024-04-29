from django.shortcuts import render

def about_me_view(request):
    # Logic to render the "About Me" page
    return render(request, 'About_Me.html')

def bikes_available_view(request):
    # Logic to render the "Bikes Available" page
    return render(request, 'Bikes_Available.html')

def user_signup_view(request):
    # Logic to render the "Login" page
    return render(request, 'signup.html')

def user_login_view(request):
    # Logic to render the "signup" page
    return render(request, 'login.html')