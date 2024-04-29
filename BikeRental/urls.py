from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='homepage.html'), name='home'),
    path('About_Me.html', views.about_me_view, name='About_Me'),
    path('Bikes_Available.html', views.bikes_available_view, name='Bikes_Available'),
    path('signup/', views.user_signup_view, name='signup'),
    path('login/', views.user_login_view, name='login'),
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),
    path('process_rental/', include('process_rental.urls')),
]
