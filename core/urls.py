from django.urls import path
from .views import home, summoner, ranktop, champs, championid

urlpatterns = [
    path('', home, name="home"),
    path('summoner/<serverid>/<summonerid>', summoner, name="summoner"),
    path('ranktop', ranktop, name="ranktop"),
    path('champion', champs, name="champs"),
    path('champion/<champid>', championid, name="championid"),
]
