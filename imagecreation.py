from PIL import Image, ImageDraw, ImageFont
from os import path
from urllib.request import urlretrieve

#from pokemon_class import pokemon

import config        
import platform
if platform.system() == 'Linux':
    import config_linux as configOS
elif platform.system() == 'Windows':
    import config_win as configOS

# download_image download the file identified by the id from files.pokefans.net if it is not downloaded already
# Args:
#   id | string:  selects pokemon and its version
#   shiny | string: if shiny is "shiny" then it downloads the shiny version instead
async def download_image(id):
    img = id + ".png"
    if not path.exists(configOS.IMAGEFOLDER + img):
        urlretrieve("https://files.pokefans.net/sprites/home/" + img, configOS.IMAGEFOLDER + img)
    im = Image.open(configOS.IMAGEFOLDER + img)
    im.save(configOS.IMAGEFOLDER + img, quality = config.QUALITY)

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
    topleft = (pos[0] - config.CIRCLEBONUS, pos[1] - config.CIRCLEBONUS)
    botright = (pos[0] + config.PKMNSIZE + config.CIRCLEBONUS, pos[1] + config.PKMNSIZE + config.CIRCLEBONUS)
    outline_color = ('white' if status == 'black' else status)
    draw.ellipse([topleft, botright], fill=status, outline=outline_color)
    return bg

# add_mons resizes and adds the image of an already downloaded pokemon to the background
# Args:
#   bg | Image: background picture where it gets drawn on
#   pkmn_id | string: id to identify what species it is. image file is named like id 
#   pos | tuple(int,int): top left corner of the pokemon image bounding box
# Returns:
#   bg_copy | image: input image added with image of the pokemon
async def add_mon(bg, pkmn_id, pos):
    im = Image.open(configOS.IMAGEFOLDER + pkmn_id + ".png")    
    if im.size != (config.PKMNSIZE, config.PKMNSIZE): im = im.resize((config.PKMNSIZE, config.PKMNSIZE))
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
    im = Image.open(configOS.SPARKLESOURCE)    
    bg_copy = bg.copy() 
    bg_copy.paste(im, (pos[0] + config.SPARKLEOFFSET, pos[1] + config.SPARKLEOFFSET), im)
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
    font = ImageFont.truetype(configOS.FONT, config.FONTSIZE)
    draw = ImageDraw.Draw(bg)
    w, h = draw.textsize(name, font)
    pos = (pos[0] + ((config.BLOCKSIZE - 2*config.TEXTOFFSET_X) - w)/2, pos[1])
    textcolor = ('white' if status == 'black' else status)
    draw.text(pos, name, font=font, align="center", fill=textcolor)
    return bg

# create_image creates a image with all the pokemon it gets as input and atleast 6 pokemon space
# Args:
#   pkmns | [pokemon_class]: list of pokemons that should be used when creating an image
# Returns:
#   bg | image: final image.
async def create_image(pkmns, min=6):
    blockcount = (len(pkmns) if len(pkmns) > min else min)

    PKMNPOS = [(config.BLOCKSIZE*i + config.PKMNOFFSET_X, config.PKMNOFFSET_Y) for i in range(blockcount)]
    TEXTPOS = [(config.BLOCKSIZE*i + config.TEXTOFFSET_X, config.TEXTOFFSET_Y) for i in range(blockcount)]

    bg = Image.new('RGBA',(blockcount*config.BLOCKSIZE, config.BLOCKSIZE),(0,0,0, 0))

    for i in range(blockcount):
        if i >= len(pkmns): break
        await(download_image(pkmns[i].id))
        bg = await(add_status(bg, pkmns[i].status, PKMNPOS[i]))
        bg = await(add_mon(bg, pkmns[i].id, PKMNPOS[i]))
        bg = (await(add_shiny_sparkle(bg, PKMNPOS[i])) if pkmns[i].id.endswith("shiny") else bg)        
        bg = await(add_name(bg, pkmns[i].name, pkmns[i].status, TEXTPOS[i]))
    return bg
