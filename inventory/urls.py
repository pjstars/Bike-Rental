from django.urls import path
from . import views

urlpatterns = [
    path('bike_inventory/', views.inventory_view, name='bike_inventory'),
    
]
