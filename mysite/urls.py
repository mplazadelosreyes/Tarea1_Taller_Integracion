"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from t1 import views

urlpatterns = [
    # ex: /t1/
    path('', views.index, name='index'),
    # click en index pa ir a episode
    path('<int:episode_id>/', views.episode, name='episode'),
    # click en episode al nombre del personaje
    path('character/<int:character_id>/', views.character, name='character'),
    # click en las locations
    path('location/<int:location_id>/', views.location, name='location'),
    # busqueda
    path('search/', views.search, name='search'),
    path('admin/', admin.site.urls),
]

