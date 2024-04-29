from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='homepage'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('bike_inventory/', views.bike_inventory, name='bike_inventory'),
    path('process_rental/', views.process_rental_request, name='process_rental'),
    path('accounts/', include('django.contrib.auth.urls')),
]
