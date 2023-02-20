# poke_api.py

import requests

def get_pokemon_info(pokemon_name):
    """
    Returns a dictionary containing information 
    about the specified Pokemon.

    Parameters
    ----------
    pokemon_name : str
        The name of the Pokemon, or its PokeDex
        number.

    Returns
    -------
    dict or None
        A dictionary containing the Pokemon's 
        information, or None if the Pokemon
        information is not fetched successfully.
    """
    pokemon_name = pokemon_name.strip().lower()
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_name)
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        print('Response code: {}'.format(r.status_code))
        return None