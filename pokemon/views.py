from django.shortcuts import render,redirect
import requests
from .models import Pokemon

def search_pokemon(request):
    pokemon_list = []
    error = None

    poke_type = request.GET.get("type")

    if poke_type:
        response = requests.get(f"https://pokeapi.co/api/v2/type/{poke_type.lower()}")

        if response.status_code == 200:
            data = response.json()

            for item in data["pokemon"][:10]:
                details = requests.get(item["pokemon"]["url"]).json()

                pokemon_list.append({
                    "name": details["name"],
                    "image": details["sprites"]["front_default"],
                    "type": poke_type.capitalize()
                })
        else : error = "Invalid Input. Pleease enter a valid pokemon type."
    return render(request, "pokemon/search.html", {
        "pokemon_list": pokemon_list,
        "error" : error})

def pokemon_detail(request, name):

    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)
    data = response.json()
    pokemon = {
        "name": data["name"], "id": data["id"],
        "image": data["sprites"]["other"]["official-artwork"]["front_default"],
        "height": data["height"],
        "weight": data["weight"],
        "base_experience": data["base_experience"],
        "types": [t["type"]["name"] for t in data["types"]],
        "abilities": [a["ability"]["name"] for a in data["abilities"]],
        "moves": [m["move"]["name"] for m in data["moves"][:5]],
    }

    return render(request, "pokemon/detail.html", {"pokemon": pokemon})

def add_to_team(request, name):

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    data = response.json()
    Pokemon.objects.create(
        name=data["name"],
        image=data["sprites"]["other"]["official-artwork"]["front_default"],
        pokemon_type=data["types"][0]["type"]["name"]
    )

    return redirect("my_team")

def my_team(request):
    team = Pokemon.objects.all()
    return render(request, "pokemon/team.html", {"team": team})
    team = Pokemon.objects.all()
    total = team.count()
    types = {}
    for pokemon in team:
     if pokemon.pokemon_type in types:
        types[pokemon.pokemon_type] += 1
     else:
        types[pokemon.pokemon_type] = 1
    if Pokemon.objects.count() >= 6:
     return redirect("my_team")

    return render(request,
              "pokemon/team.html",
              {   "team": team,
                  "total": total,
                  "types": types})


