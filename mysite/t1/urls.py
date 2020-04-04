from django.urls import path

from . import views

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
]