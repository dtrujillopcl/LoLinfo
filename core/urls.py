from django.urls import path
from .views import home, summoner

urlpatterns = [
    path('', home, name="home"),
    path('summoner/<serverid>/<summonerid>', summoner, name="summoner"),
]
