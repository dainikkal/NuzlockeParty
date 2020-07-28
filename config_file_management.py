import asyncio
from os import path

import config
import platform
if platform.system() == 'Linux':
    import config_linux as configOS
elif platform.system() == 'Windows':
    import config_win as configOS

CONFIG_FILE = "data/config.txt"

async def load_configs():
    if not path.exists(CONFIG_FILE):
        return
    with open(CONFIG_FILE,'r') as f:
        Lines = f.readlines()

        for line in Lines:
            l = line.split(" ",1)
            if len(l) == 1 : continue
            config_code = l[0]
            config_setting = l[1]
            if config_code == "SPREAD" : config.SPREAD = config_setting
            if config_code == "SHEET" : config.SHEET = config_setting

            if config_code == "BLOCKSIZE" : config.BLOCKSIZE = int(config_setting)

            if config_code == "PKMNSIZE" : config.PKMNSIZE = int(config_setting)
            if config_code == "PKMNAREA" : 
                config.PKMNAREA = (config.PKMNSIZE,config.PKMNSIZE)
            if config_code == "PKMNOFFSET_X" : config.PKMNOFFSET_X = int(config_setting)
            if config_code == "PKMNOFFSET_Y" : config.PKMNOFFSET_Y = int(config_setting)

            if config_code == "CIRCLEBONUS" : config.CIRCLEBONUS = int(config_setting)

            if config_code == "TEXTOFFSET_X" : config.TEXTOFFSET_X = int(config_setting)
            if config_code == "TEXTOFFSET_Y" : config.TEXTOFFSET_Y = int(config_setting)
            
            if config_code == "SPARKLEOFFSET" : config.SPARKLEOFFSET = int(config_setting)

            if config_code == "QUALITY" : config.QUALITY = int(config_setting)

            if config_code == "COLOR_ALIVE" : config.COLOR_ALIVE = config_setting
            if config_code == "COLOR_DEAD" : config.COLOR_DEAD = config_setting
            if config_code == "COLOR_PARTY" : config.COLOR_PARTY = config_setting
            if config_code == "COLOR_MISSED" : config.COLOR_MISSED = config_setting
            if config_code == "COLOR_RELEASED" : config.COLOR_RELEASED = config_setting
            if config_code == "COLOR_DAY_CARE" : config.COLOR_DAY_CARE = config_setting
            if config_code == "COLOR_PENDING" : config.COLOR_PENDING = config_setting

            if config_code == "SPARKLESOURCE" : configOS.SPARKLEOFFSET = config_setting

            if config_code == "IMAGEFOLDER" : configOS.IMAGEFOLDER = config_setting
            if config_code == "PARTYDESTINATION" : configOS.PARTYDESTINATION = config_setting
            if config_code == "OTHERMONSDESTINATION" : configOS.OTHERMONSDESTINATION = config_setting
            
            if config_code == "FONT" : configOS.FONT = config_setting
            if config_code == "FONTSIZE" : config.FONTSIZE = int(config_setting)


async def write_configs():
    lines = [] 
    lines.append("SPREAD " + config.SPREAD)
    lines.append("SHEET " + config.SHEET)
    
    lines.append("BLOCKSIZE "+ str(config.BLOCKSIZE))

    lines.append("PKMNSIZE "+ str(config.PKMNSIZE))
    lines.append("PKMNSOFFSET_X "+ str(config.PKMNOFFSET_X))
    lines.append("PKMNSOFFSET_Y "+ str(config.PKMNOFFSET_Y))

    lines.append("CIRCLEBONUS "+ str(config.CIRCLEBONUS))

    lines.append("TEXTOFFSET_X "+ str(config.TEXTOFFSET_X))
    lines.append("TEXTOFFSET_Y "+ str(config.TEXTOFFSET_Y))
    
    lines.append("SPARKLEOFFSET "+ str(config.SPARKLEOFFSET))

    lines.append("QUALITY "+ str(config.QUALITY))

    lines.append("COLOR_ALIVE "+ config.COLOR_ALIVE)
    lines.append("COLOR_DEAD "+ config.COLOR_DEAD)
    lines.append("COLOR_PARTY "+ config.COLOR_PARTY)
    lines.append("COLOR_MISSED "+ config.COLOR_MISSED)
    lines.append("COLOR_RELEASED "+ config.COLOR_RELEASED)
    lines.append("COLOR_DAY_CARE "+ config.COLOR_DAY_CARE)
    lines.append("COLOR_PENDING "+ config.COLOR_PENDING)

    lines.append("SPARKLESOURCE " +  configOS.SPARKLESOURCE)

    lines.append("IMAGEFOLDER " +  configOS.IMAGEFOLDER)
    lines.append("PARTYDESTINATION " +  configOS.PARTYDESTINATION)
    lines.append("OTHERMONDESTINATION " +  configOS.OTHERMONSDESTINATION)
    
    lines.append("FONT " +  configOS.FONT)
    lines.append("FONTSIZE " +  str(config.FONTSIZE))

    return [x+"\n" for x in lines]

async def save_config():
    with open(CONFIG_FILE, "w") as f:
        f.writelines(await(write_configs()))
