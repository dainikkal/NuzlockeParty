from PIL import Image, ImageDraw, ImageFont
from os import path
from urllib.request import urlretrieve

import pokemon_class

#import config
from config import BLOCKSIZE, \
    PKMNSIZE, PKMNAREA, \
    PKMNOFFSET_X, PKMNOFFSET_Y, \
    CIRCLEBONUS, \
    TEXTOFFSET_X, TEXTOFFSET_Y, \
    SPARKLEOFFSET, \
    SPARKLESOURCE, \
    IMAGEFOLDER, \
    QUALITY, \
    FONT \

# download_image download the file identified by the id from files.pokefans.net if it is not downloaded already
# Args:
#   id | string:  selects pokemon and its version
#   shiny | string: if shiny is "shiny" then it downloads the shiny version instead
async def download_image(id):
    img = id + ".png"
    if not path.exists(IMAGEFOLDER + img):
        urlretrieve("https://files.pokefans.net/sprites/home/" + img, IMAGEFOLDER + img)
    im = Image.open(IMAGEFOLDER + img)
    if im.size != PKMNAREA: im = im.resize(PKMNAREA)
    im.save(IMAGEFOLDER + img, quality = QUALITY)

# add_status adds  the circle in the background which indicates the status of the mon. when black is used it turns 
#    creates an border in white
# Args:
#    bg | Image: background picture where it gets drawn on
#    status | string: color string indicating the used color
#    pos | tuple(int,int): top left corner of the pokemon image bounding box
# Returns:
#   bg_copy | image: input image added with circle with color based on the status
async def add_status(bg, status, pos):
    draw = ImageDraw.Draw(bg)
    topleft = (pos[0] - CIRCLEBONUS, pos[1] - CIRCLEBONUS)
    botright = (pos[0] + PKMNSIZE + CIRCLEBONUS, pos[1] + PKMNSIZE + CIRCLEBONUS)
    outline_color = ('white' if status == 'black' else status)
    draw.ellipse([topleft, botright], fill=status, outline=outline_color)
    return bg

# add_mons adds the image of an already downloaded pokemon to the background
# Args:
#   bg | Image: background picture where it gets drawn on
#   pkmn_id | string: id to identify what species it is. image file is named like id 
#   pos | tuple(int,int): top left corner of the pokemon image bounding box
# Returns:
#   bg_copy | image: input image added with image of the pokemon
async def add_mon(bg, pkmn_id, pos):
    im = Image.open(IMAGEFOLDER + pkmn_id + ".png")    
    bg_copy = bg.copy()
    bg_copy.paste(im, pos, im)
    return bg_copy

# add_shiny_sparkle adds a shiny sparkle to pokemon with the sparkle offset
# Args:
#   bg | Image: background picture where it gets drawn on
#   pos | tuple(int,int): top left corner of the pokemon image bounding box
# Returns:
#   bg_copy | image: input image added with the shiny sparkle
async def add_shiny_sparkle(bg, pos):
    im = Image.open(SPARKLESOURCE)    
    bg_copy = bg.copy() 
    bg_copy.paste(im, (pos[0] + SPARKLEOFFSET, pos[1] + SPARKLEOFFSET), im)
    return bg_copy

# add_name adds the name of the Pokemon underneath the image, it is colored based on status, 
#   if status is black it will be in white
# Args:
#   bg | Image: background picture where it gets drawn on
#   name | string: name of the Pokemon
#   status | string: color string indicating the used color
#   pos | tuple(int,int): top left corner of the pokemon image bounding box
# Returns:
#   bg | image: image of the input with name added
async def add_name(bg, name, status, pos):
    font = ImageFont.truetype(FONT, 27)
    draw = ImageDraw.Draw(bg)
    w, h = draw.textsize(name, font)
    pos = (pos[0] + ((BLOCKSIZE - 2*TEXTOFFSET_X) - w)/2, pos[1])
    textcolor = ('white' if status == 'black' else status)
    draw.text(pos, name, font=font, align="center", fill=textcolor)
    return bg

# create_image creates a image with all the pokemon it gets as input and atleast 6 pokemon space
# Args:
#   pkmns | [pokemon_class]: list of pokemons that should be used when creating an image
# Returns:
#   bg | image: final image.
async def create_image(pkmns):
    blockcount = (len(pkmns) if len(pkmns) > 6 else 6)

    PKMNPOS = [(BLOCKSIZE*i + PKMNOFFSET_X, PKMNOFFSET_Y) for i in range(blockcount)]
    TEXTPOS = [(BLOCKSIZE*i + TEXTOFFSET_X, TEXTOFFSET_Y) for i in range(blockcount)]

    bg = Image.new('RGBA',(blockcount*BLOCKSIZE, BLOCKSIZE),(0,0,0, 0))

    for i in range(blockcount):
        if i >= len(pkmns): break
        await(download_image(pkmns[i].id))
        bg = await(add_status(bg, pkmns[i].status, PKMNPOS[i]))
        bg = await(add_mon(bg, pkmns[i].id, PKMNPOS[i]))
        bg = (await(add_shiny_sparkle(bg, PKMNPOS[i])) if pkmns[i].id.endswith("shiny") else bg)        
        bg = await(add_name(bg, pkmns[i].name, pkmns[i].status, TEXTPOS[i]))
    return bg
