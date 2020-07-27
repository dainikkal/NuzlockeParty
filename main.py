import gspread 
import asyncio
from itertools import chain
from PIL import Image

from spinner import spin
from pokemon_class import pokemon
from imagecreation import create_image
from config_file_management import load_configs, write_configs

from config import \
        SPREAD, SHEET,\
        QUALITY\

import platform
if platform.system() == 'Linux':
    from config_linux import \
        PARTYDESTINATION,\
        OTHERMONSDESTINATION
elif platform.system() == 'Windows':
    from config_win import \
        PARTYDESTINATION,\
        OTHERMONSDESTINATION

# get_poke_dict creates the dictionary that maps pokemon names to their ids(pokedex-variation)
# Args:
#   ws | worksheet: Worksheet on gsheet that holds the map from Pokemon name to pokemon id
# Return:
#   pkmn_dict | {String : String}: dictrionary that maps pokemon names to their ids (pokedex-variation)
async def get_poke_dict(ws):

    pkmn_dict = {}
    pkmn_name = ws.col_values(1)
    pkmn_ids = ws.col_values(2)

    for name, id in zip(pkmn_name, pkmn_ids):
        pkmn_dict[name] = id
    return pkmn_dict

# get_images sorts all pokemon by their status, and calls the create_image() function to create a image for party and the other mons.
# Args:
#   pkmn_dict | {String : String}: dictrionary that maps pokemon names to their ids (pokedex-variation)
#   ws | worksheet: Worksheet on gsheet that holds all the information of the pokemons
async def get_images(pkmn_dict, ws):
    party = []
    alive = []
    missed = []
    dead = []
    released = []
    day_care = []
    pending =  []

    for i in range(2, 2000):
        row = ws.row_values(i)
        if row[1] == "":
            break
        
        if row[3] == "": continue
        id = pkmn_dict[row[3]]
        name  = row[0]
        status = row[1]
        shiny = row[5] 
        mon = pokemon(id, name, status, shiny)
        if   status == "party":     party.append(mon)
        elif status == "alive":     alive.append(mon)
        elif status == "missed":    missed.append(mon)
        elif status == "dead":      dead.append(mon)
        elif status == "released":  released.append(mon)
        elif status == "day care":  day_care.append(mon)
        elif status == "pending":   pending.append(mon)

    others = []
    [others.extend(mon_list) for mon_list in [pending, alive, day_care, dead, released, missed, party[6:]]]
    party = party[:6]

    im_party = await create_image(party)
    im_party.save(PARTYDESTINATION, quality = QUALITY)

    im_others = await create_image(others)
    im_others.save(OTHERMONSDESTINATION, quality = QUALITY)

# imggen loop infinitly long and looks if there are changes in the last dataset a picture was generated vs the current one and calls get_images().
# Args:
#   pkmn_dict | {String : String}: dictrionary that maps pokemon names to their ids (pokedex-variation)
#   ws | worksheet: Worksheet on gsheet that holds all the information of the pokemons
async def img_gen_main(pkmn_dict, ws):    
    old_values = [] 
    while(True):
        new_values = ws.get_all_values()
        old_con_values = list(chain.from_iterable(old_values))
        new_con_values = list(chain.from_iterable(new_values))

        same_length = len(new_values) == len(old_values)# false
        same_values = [(True if x == y else False) for x, y in zip(new_con_values, old_con_values)]
        if not same_length or (False in same_values):
            await get_images(pkmn_dict, ws)
            old_values = new_values

        await asyncio.sleep(7)

# main gets the spreadsheet, calls get_poke_dict and calls the img_gen loop
async def main():
    await load_configs()
    gc = gspread.service_account()
    sh = gc.open(SPREAD)

    ws = sh.worksheet('Pokemon')
    pkmn_dict = await(get_poke_dict(ws))
    ws = sh.worksheet(SHEET)

    await asyncio.gather(spin(), img_gen_main(pkmn_dict, ws))

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass    
    except Exception as e:
        print(e)