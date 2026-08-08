from django.urls import path
from . import views
urlpatterns = [path('', views.search_pokemon, name='search'),
               path("pokemon/<str:name>/", views.pokemon_detail, name="pokemon_detail"),
]