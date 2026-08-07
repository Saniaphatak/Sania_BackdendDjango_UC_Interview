from django.shortcuts import render
import requests

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
        "error" : error


    })
