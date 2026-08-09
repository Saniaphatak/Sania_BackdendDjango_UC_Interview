from django.urls import path
from . import views
urlpatterns = [path('', views.search_pokemon, name='search'),
               path("pokemon/<str:name>/", views.pokemon_detail, name="pokemon_detail"),
               path("add/<str:name>/", views.add_to_team, name="add_to_team"),
               path("my-team/", views.my_team, name="my_team"),
]