"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path  # important for path
from . import views  # important for calling functions present in views
import requests

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('analyse', views.analyse, name='analyse'),
    path('ex1', views.ex1, name='ex1'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('api', views.get_data_from_api, name='api')

    #path('removepunc', views.removepunc, name='removepunc'),

]
