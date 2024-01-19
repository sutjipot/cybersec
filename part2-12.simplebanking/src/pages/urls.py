from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import homePageView, addView

urlpatterns = [
    # Home page
    path('', homePageView, name='home'),
    
    # Add account
    path('add/', addView, name='add'),
    
    
]
