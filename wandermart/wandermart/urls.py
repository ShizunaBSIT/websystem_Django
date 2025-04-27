"""
URL configuration for wandermart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView, TemplateView  # Use RedirectView for redirection

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='account_login', permanent=False), name='home'),  # Redirect to login
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Ensure this is correctly included
    path('welcome/', TemplateView.as_view(template_name='home.html'), name='home'),
    
    # Add your other app URLs here, e.g.:
    # path('yourapp/', include('yourapp.urls')),
]
