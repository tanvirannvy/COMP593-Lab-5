
# pokemon_paste.py

import pastebin_api
import poke_api
import sys

def get_pokemon_name():
    """
    Gets the Pokemon name from the command line
    parameters.
    """
    if len(sys.argv) == 1:
        print('Pokemon name must be specified.')
        sys.exit(1)
    return sys.argv[1]

def construct_paste_title(pokemon_name):
    """
    Constructs the title for the paste.
    """
    return '{}\'s Abilities'.format(pokemon_name.capitalize())

def construct_paste_body(pokemon_info):
    """
    Constructs the body for the paste.
    """
    abilities = pokemon_info['abilities']
    body = ''
    for ability in abilities:
        body += '{}\n'.format(ability['ability']['name'])
    return body.strip()

def main():
    pokemon_name = get_pokemon_name()
    print('Getting information for {}...'.format(pokemon_name), end='')
    pokemon_info = poke_api.get_pokemon_info(pokemon_name)
    if pokemon_info is None:
        print('failure')
        sys.exit(1)
    else:
        print('success')
    title = construct_paste_title(pokemon_name)
    body = construct_paste_body(pokemon_info)
    print('Posting new paste to PasteBin...', end='')
    paste_url = pastebin_api.create_paste(title, body, 7, False)
    if paste_url is None:
        print('failure')
        sys.exit(1)
    else:
        print('success')
    print(paste_url)

if __name__ == '__main__':
    main()