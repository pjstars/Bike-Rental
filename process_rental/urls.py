from django.urls import path
from . import views

urlpatterns = [
    path('process_rental/', views.process_rental_view, name='process_rental'),
   
]
