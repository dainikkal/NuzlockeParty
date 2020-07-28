import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import asyncio

from pokemon_class import pokemon
from imagecreation import create_image

import config
import platform
if platform.system() == 'Linux':
    import config_linux as configOS
    FOLDERSEP = "/"
elif platform.system() == 'Windows':
    import config_win as configOS
    FOLDERSEP = "\\"

root = tk.Tk()
root.title("Nuzlocke Party Config")

var_blocksize = tk.StringVar()
var_blocksize.set(config.BLOCKSIZE)
def changeBlockSize():
    try:
        number = int(var_blocksize.get())
    except:
        return False
    config.BLOCKSIZE = number
    updateImg()
    return True

var_pkmnsize = tk.StringVar()
var_pkmnsize.set(config.PKMNSIZE)
def changePkmnSize():
    try:
        config.PKMNSIZE = int(var_pkmnsize.get())
        config.PKMNAREA = (config.PKMNSIZE, config.PKMNSIZE)
        updateImg()
        return True
    except:
        return False

var_PkmnOffsetX = tk.StringVar()
var_PkmnOffsetX.set(config.PKMNOFFSET_X)
def changePkmnOffsetX():
    try:
        config.PKMNOFFSET_X = int(var_PkmnOffsetX.get())
        updateImg()
        return True
    except:
        return False

var_PkmnOffsetY = tk.StringVar()
var_PkmnOffsetY.set(config.PKMNOFFSET_Y)
def changePkmnOffsetY():
    try:
        config.PKMNOFFSET_Y = int(var_PkmnOffsetY.get())
        updateImg()
        return True
    except:
        return False

var_CircleBonus = tk.StringVar()
var_CircleBonus.set(config.CIRCLEBONUS)
def changeCircleBonus():
    try:
        config.CIRCLEBONUS = int(var_CircleBonus.get())
        updateImg()
        return True
    except:
        return False

var_TextOffsetX = tk.StringVar()
var_TextOffsetX.set(config.TEXTOFFSET_X)
def changeTextOffsetX():
    try:
        config.TEXTOFFSET_X = int(var_TextOffsetX.get())
        updateImg()
        return True
    except:
        return False

var_TextOffsetY = tk.StringVar()
var_TextOffsetY.set(config.TEXTOFFSET_Y)
def changeTextOffsetY():
    try:
        config.TEXTOFFSET_Y = int(var_TextOffsetY.get())
        updateImg()
        return True
    except:
        return False

var_SparkleOffset = tk.StringVar()
var_SparkleOffset.set(config.SPARKLEOFFSET)
def changeSparkleOffset():
    try:
        config.SPARKLEOFFSET = int(var_SparkleOffset.get())
        updateImg()
        return True
    except:
        return False

var_FontSize = tk.StringVar()
var_FontSize.set(config.FONTSIZE)
def changeFontSize():
    try:
        config.FONTSIZE = int(var_FontSize.get())
        updateImg()
        return True
    except:
        return False

var_font = tk.StringVar()
var_font.set(configOS.FONT.split(FOLDERSEP)[-1])
def openFont(): 
    fontname = filedialog.askopenfilename(title = "Select file", filetypes=(("font file", "*.ttf"),("all files","*-*")))
    if fontname != "": configOS.FONT = fontname.replace("/",FOLDERSEP)
    var_font.set(configOS.FONT.split(FOLDERSEP)[-1])
    updateImg()

var_sparkle = tk.StringVar()
var_sparkle.set(configOS.SPARKLESOURCE.split(FOLDERSEP)[-1])
def openSparkle(): 
    spaklename = filedialog.askopenfilename(title = "Select file", filetypes=(("PNG file", "*.png"),("all files","*-*")))
    if spaklename != "": configOS.SPARKLESOURCE = spaklename.replace("/",FOLDERSEP)
    var_sparkle.set(configOS.SPARKLESOURCE.split(FOLDERSEP)[-1])

var_party = tk.StringVar()
var_party.set(configOS.PARTYDESTINATION.split(FOLDERSEP)[-1])
def saveParty(): 
    partydest = filedialog.asksaveasfilename(title = "Save As", filetypes=(("PNG file", "*.png"),("all files","*-*")))
    if partydest != "": configOS.PARTYDESTINATION = partydest.replace("/",FOLDERSEP)
    var_party.set(configOS.PARTYDESTINATION.split(FOLDERSEP)[-1])
    
var_othermons = tk.StringVar()
var_othermons.set(configOS.OTHERMONSDESTINATION.split(FOLDERSEP)[-1])
def saveOtherMons(): 
    othermondest = filedialog.asksaveasfilename(title = "Save As", filetypes=(("PNG file", "*.png"),("all files","*-*")))
    if othermondest != "": configOS.OTHERMONSDESTINATION = othermondest.replace("/",FOLDERSEP)
    var_othermons.set(configOS.OTHERMONSDESTINATION.split(FOLDERSEP)[-1])

#Preview pokemon
SAMPLE_MON = pokemon("0475-000","He Protect","party",True)
def updateImg():    
    #getimage()
    temp_img =  asyncio.run(create_image([SAMPLE_MON], min=1))
    img2 = ImageTk.PhotoImage(temp_img)
    label_preview.configure( width=config.BLOCKSIZE, height=config.BLOCKSIZE,image=img2)
    label_preview.image = img2
        

#OBJECTS
frame_spreadsheet = tk.Frame(root)
label_spread = tk.Label(frame_spreadsheet, text="Spreadsheet name:")
entry_spread = tk.Entry(frame_spreadsheet)

label_sheet = tk.Label(frame_spreadsheet, text="Sheet page name:")
entry_sheet = tk.Entry(frame_spreadsheet)

seperator_1 = ttk.Separator(root, orient=tk.HORIZONTAL)
frame_previewblock = tk.Frame(root)

frame_preview = tk.Frame(frame_previewblock)
temp_img = asyncio.run(create_image([SAMPLE_MON], min=1))
#temp_img = Image.new("RGBA",(150,150),"black")
img = ImageTk.PhotoImage(temp_img)
label_preview = tk.Label(frame_preview,  width= config.BLOCKSIZE, height=config.BLOCKSIZE,image=img)

label_Blocksize = tk.Label(frame_previewblock, text="Blocksize:")
entry_Blocksize = tk.Entry(frame_previewblock, textvariable=var_blocksize, validate="focusout", validatecommand=changeBlockSize)
label_PkmnSize = tk.Label(frame_previewblock, text="Pokemon Size:")
entry_PkmnSize = tk.Entry(frame_previewblock, textvariable=var_pkmnsize, validate="focusout", validatecommand=changePkmnSize)
label_PkmnOffsetX = tk.Label(frame_previewblock, text="Pokemon Offset(X):")
entry_PkmnOffsetX = tk.Entry(frame_previewblock, textvariable=var_PkmnOffsetX, validate="focusout", validatecommand=changePkmnOffsetX)
label_PkmnOffsetY = tk.Label(frame_previewblock, text="Pokemon Offset(Y):")
entry_PkmnOffsetY = tk.Entry(frame_previewblock, textvariable=var_PkmnOffsetY, validate="focusout", validatecommand=changePkmnOffsetY)
label_CircleBonus = tk.Label(frame_previewblock, text="Circle Extension:")
entry_CircleBonus = tk.Entry(frame_previewblock, textvariable=var_CircleBonus, validate="focusout", validatecommand=changeCircleBonus)
label_TextOffsetX = tk.Label(frame_previewblock, text="Text Offset(X):")
entry_TextOffsetX = tk.Entry(frame_previewblock, textvariable=var_TextOffsetX, validate="focusout", validatecommand=changeTextOffsetX)
label_TextOffsetY = tk.Label(frame_previewblock, text="Text Offset(Y):")
entry_TextOffsetY = tk.Entry(frame_previewblock, textvariable=var_TextOffsetY, validate="focusout", validatecommand=changeTextOffsetY)

label_Font = tk.Label(frame_previewblock, text="Font")
button_Font = tk.Button(frame_previewblock, text="Select Fontfile", command = openFont)
label_SelectedFontAnswer = tk.Label(frame_previewblock, textvariable=var_font)

label_FontSize = tk.Label(frame_previewblock, text="Font Size:")
entry_FontSize = tk.Entry(frame_previewblock, textvariable=var_FontSize, validate="focusout", validatecommand=changeFontSize)

label_SparkleOffset = tk.Label(frame_previewblock, text="Sparkle Offset:")
entry_SparkleOffset = tk.Entry(frame_previewblock, textvariable=var_SparkleOffset, validate="focusout", validatecommand=changeSparkleOffset)

label_SparkleFile = tk.Label(frame_previewblock, text="Sparkle")
button_SparkleFile = tk.Button(frame_previewblock, text="Select Sparklefile", command = openSparkle)
label_SelectedSparkleFileAnswer = tk.Label(frame_previewblock, textvariable=var_sparkle)

seperator_2 = ttk.Separator(root, orient=tk.HORIZONTAL)
frame_destinationblock = tk.Frame(root)

label_PartyFile = tk.Label(frame_destinationblock, text="Party Dest:")
button_PartyFile = tk.Button(frame_destinationblock, text="Select Party Dest", command = saveParty)
label_SelectedPartyFileAnswer = tk.Label(frame_destinationblock, textvariable=var_party)
label_OtherMonsFile = tk.Label(frame_destinationblock, text="Other Pokemons Dest:")
button_OtherMonsFile = tk.Button(frame_destinationblock, text="Select Other Pokemon Dest", command = saveOtherMons)
label_SelectedOtherMonsFileAnswer = tk.Label(frame_destinationblock, textvariable=var_othermons)


#INSERT VALUES
entry_spread.insert(0,config.SPREAD)
entry_sheet.insert(0,config.SHEET)


#CONFIGS
labels_spreadsheet = [label_spread, label_sheet]
entrys_spreadsheet = [entry_spread, entry_sheet]

labels_previewblock = [label_Blocksize, label_PkmnSize, label_PkmnOffsetX, label_PkmnOffsetY, \
    label_PkmnOffsetY, label_CircleBonus, label_TextOffsetX, label_TextOffsetY, label_Font, \
    label_FontSize, label_SparkleOffset, label_SparkleFile]
inputs_previewblock = [entry_Blocksize, entry_PkmnSize, entry_PkmnOffsetX, entry_PkmnOffsetY, \
    entry_PkmnOffsetY, entry_CircleBonus, entry_TextOffsetX, entry_TextOffsetY, \
    button_Font, entry_FontSize, entry_SparkleOffset, button_SparkleFile]
labels_previewblockFiles = [label_SelectedFontAnswer, label_SelectedSparkleFileAnswer]

labels_destination = [label_PartyFile, label_OtherMonsFile]
inputs_destination = [button_PartyFile, button_OtherMonsFile]
labels_destination_answers = [label_SelectedPartyFileAnswer, label_SelectedOtherMonsFileAnswer]

[x.config(width=20, anchor='w', font=("bold",10)) for x in labels_spreadsheet + labels_previewblock +\
    labels_previewblockFiles + labels_destination + labels_destination_answers]
[x.config(width=20) for x in entrys_spreadsheet + inputs_previewblock + inputs_destination]


#Grid
frame_spreadsheet.grid(row=0, column=0, sticky = "w")
[x.grid(row=num,column=0) for num, x in zip(range(len(labels_spreadsheet)), labels_spreadsheet)]
[x.grid(row=num,column=1) for num, x in zip(range(len(entrys_spreadsheet)), entrys_spreadsheet)]

seperator_1.grid(row=1, column=0, sticky="we")
frame_previewblock.grid(row=2, column=0, sticky = "w")

[x.grid(row=num,column=0) for num, x in zip(range(len(labels_previewblock)), labels_previewblock)]
[x.grid(row=num,column=1) for num, x in zip(range(len(inputs_previewblock)), inputs_previewblock)]
label_SelectedFontAnswer.grid(row=9, column=2)
label_SelectedSparkleFileAnswer.grid(row=11, column=2)

frame_preview.grid(row=0, column=2, rowspan=6)
label_preview.grid(row=0, column=0)
seperator_2.grid(row=3, column=0, sticky="ew")
frame_destinationblock.grid(row=4, column=0, sticky = "w")

[x.grid(row=num,column=0) for num, x in zip(range(len(labels_destination)), labels_destination)]
[x.grid(row=num,column=1) for num, x in zip(range(len(inputs_destination)), inputs_destination)]
[x.grid(row=num,column=2) for num, x in zip(range(len(labels_destination_answers)), labels_destination_answers)]

root.mainloop()