import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, colorchooser
from PIL import Image, ImageTk
import asyncio

import tk_object as tkobj
from pokemon_class import pokemon
from imagecreation import create_image
from multiprocessing import Process
from config_file_management import load_configs, save_config
from runner import init as initRunner

import platform
import config
if platform.system() == 'Linux':
    import config_linux as configOS
    FOLDERSEP = "/"
elif platform.system() == 'Windows':
    import config_win as configOS
    FOLDERSEP = "\\"

class NuzlockeParty:
    # init_var initializes variables for the inputs 
    def init_var(self):
        self.var_Spread = tk.StringVar(value=config.SPREAD)
        self.var_Sheet = tk.StringVar(value=config.SHEET)
        self.var_BlockSize = tk.StringVar(value=config.BLOCKSIZE)
        self.var_PkmnSize = tk.StringVar(value=config.PKMNSIZE)
        self.var_PkmnOffsetX = tk.StringVar(value=config.PKMNOFFSET_X)
        self.var_PkmnOffsetY = tk.StringVar(value=config.PKMNOFFSET_Y)
        self.var_CircleBonus = tk.StringVar(value=config.CIRCLEBONUS)
        self.var_TextOffsetX = tk.StringVar(value=config.TEXTOFFSET_X)
        self.var_TextOffsetY = tk.StringVar(value=config.TEXTOFFSET_Y)
        self.var_SparkleOffset = tk.StringVar(value=config.SPARKLEOFFSET)
        self.var_FontSize = tk.StringVar(value=config.FONTSIZE)
        self.var_Font = tk.StringVar(value=configOS.FONT.split(FOLDERSEP)[-1])
        self.var_Sparkle = tk.StringVar(value=configOS.SPARKLESOURCE.split(FOLDERSEP)[-1])
        self.var_Party = tk.StringVar(value=configOS.PARTYDESTINATION.split(FOLDERSEP)[-1])
        self.var_OtherMons = tk.StringVar(value=configOS.OTHERMONSDESTINATION.split(FOLDERSEP)[-1])
        self.var_Color = tk.StringVar(value="party")

    # init_top_level initializes frames and seperator directly on the root
    def init_top_level(self):
        self.frame_0 = tkobj.tk_frame(self.master, 0, 0, "w").getObj()
        tkobj.tk_seperator(self.master, 1, 0, "ew", tk.HORIZONTAL)
        self.frame_1 = tkobj.tk_frame(self.master, 2, 0, "w").getObj()
        tkobj.tk_seperator(self.master, 3, 0, "ew", tk.HORIZONTAL)
        self.frame_2 = tkobj.tk_frame(self.master, 4, 0, "w").getObj()
        tkobj.tk_seperator(self.master, 5, 0, "ew", tk.HORIZONTAL)
        self.frame_3 = tkobj.tk_frame(self.master, 6, 0, "w").getObj()
        tkobj.tk_seperator(self.master, 7, 0, "ew", tk.HORIZONTAL)
        self.frame_4 = tkobj.tk_frame(self.master, 8, 0, "w").getObj()

    # init_spreadsheet initializes input and labels for the spreadsheet information
    def init_spreadsheet(self):
        tkobj.tk_labelNoIO(self.frame_0, 0, 0, 20, "Spreadsheet name:", "w", self.font)
        tkobj.tk_labelNoIO(self.frame_0, 1, 0, 20, "Sheet page name:", "w", self.font)
        tkobj.tk_Entry(self.frame_0, 0, 1, 20, self.var_Spread, "focusout", lambda : self.changeValue("SPREAD", self.var_Spread))
        tkobj.tk_Entry(self.frame_0, 1, 1, 20, self.var_Sheet, "focusout", lambda : self.changeValue("SHEET", self.var_Sheet))

    # init_preview initializes frame and image for the image preview
    def init_preview(self):
        self.frame_preview = tkobj.tk_frame(self.frame_1, 0, 2, "e", 6).getObj()
        img = ImageTk.PhotoImage(Image.new("RGBA",(config.BLOCKSIZE,config.BLOCKSIZE),"black"))
        self.img_preview = tkobj.tk_LabelIMG(self.frame_preview, 0, 0, config.BLOCKSIZE, config.BLOCKSIZE, img).getObj()

    # init_image initializes input and labels for the image information
    def init_image(self):
        tkobj.tk_labelNoIO(self.frame_1, 0, 0, 20, "Blocksize:", "w", self.font)
        tkobj.tk_labelNoIO(self.frame_1, 1, 0, 20, "Pokemon Size:", "w", self.font)
        tkobj.tk_labelNoIO(self.frame_1, 2, 0, 20, "Pokemon Offset(X):", "w", self.font)
        tkobj.tk_labelNoIO(self.frame_1, 3, 0, 20, "Pokemon Offset(Y):", "w", self.font)
        tkobj.tk_labelNoIO(self.frame_1, 4, 0, 20, "Circle Extension:", "w", self.font)
        tkobj.tk_labelNoIO(self.frame_1, 5, 0, 20, "Text Offset(X):", "w", self.font)
        tkobj.tk_labelNoIO(self.frame_1, 6, 0, 20, "Text Offset(Y):", "w", self.font)
        tkobj.tk_labelNoIO(self.frame_1, 7, 0, 20, "Font: ", "w", self.font)
        tkobj.tk_labelNoIO(self.frame_1, 8, 0, 20, "Font Size:", "w", self.font)
        tkobj.tk_labelNoIO(self.frame_1, 9, 0, 20, "Sparkle: ", "w", self.font)
        tkobj.tk_labelNoIO(self.frame_1, 10, 0, 20, "Sparkle Offset:", "w", self.font)
        tkobj.tk_Entry(self.frame_1, 0, 1, 20, self.var_BlockSize, "focusout", lambda : self.changeValue("BLOCKSIZE", self.var_BlockSize))
        tkobj.tk_Entry(self.frame_1, 1, 1, 20, self.var_PkmnSize, "focusout", lambda : self.changeValue("PKMNSIZE", self.var_PkmnSize))
        tkobj.tk_Entry(self.frame_1, 2, 1, 20, self.var_PkmnOffsetX, "focusout", lambda : self.changeValue("PKMNOFFSET_X", self.var_PkmnOffsetX))
        tkobj.tk_Entry(self.frame_1, 3, 1, 20, self.var_PkmnOffsetY, "focusout", lambda : self.changeValue("PKMNOFFSET_Y", self.var_PkmnOffsetY))
        tkobj.tk_Entry(self.frame_1, 4, 1, 20, self.var_CircleBonus, "focusout", lambda : self.changeValue("CIRCLEBONUS", self.var_CircleBonus))
        tkobj.tk_Entry(self.frame_1, 5, 1, 20, self.var_TextOffsetX, "focusout", lambda : self.changeValue("TEXTOFFSET_X", self.var_TextOffsetX))
        tkobj.tk_Entry(self.frame_1, 6, 1, 20, self.var_TextOffsetY, "focusout", lambda : self.changeValue("TEXTOFFSET_Y", self.var_TextOffsetY))
        tkobj.tk_Button(self.frame_1, 7, 1, 20, "Select Fontfile", lambda : self.fileIO("FONT", self.var_Font, filedialog.askopenfilename, ("font file", "*.ttf")))
        tkobj.tk_Entry(self.frame_1, 8, 1, 20, self.var_FontSize, "focusout", lambda : self.changeValue("FONTSIZE", self.var_FontSize))
        tkobj.tk_Button(self.frame_1, 9, 1, 20, "Select Sparklefile", lambda : self.fileIO("SPARKLESOURCE", self.var_Sparkle, filedialog.askopenfilename, ("PNG file", "*.png")))
        tkobj.tk_Entry(self.frame_1, 10, 1, 20, self.var_SparkleOffset, "focusout", lambda : self.changeValue("SPARKLEOFFSET", self.var_SparkleOffset))
        tkobj.tk_LabelIO(self.frame_1, 7, 2, 20, self.var_Font, "w", self.font)
        tkobj.tk_LabelIO(self.frame_1, 9, 2, 20, self.var_Sparkle, "w", self.font)

    # init_color initializes input and labels for color settings 
    def init_color(self):
        self.label_alive = tkobj.tk_labelColor(self.frame_2, 0, 0, 20, "Color Alive:", "w", self.font, fg=config.COLOR_ALIVE).getObj()
        self.label_dead = tkobj.tk_labelColor(self.frame_2, 1, 0, 20, "Color Dead:", "w", self.font, fg=config.COLOR_DEAD).getObj()
        self.label_party = tkobj.tk_labelColor(self.frame_2, 2, 0, 20, "Color Party:", "w", self.font, fg=config.COLOR_PARTY).getObj()
        self.label_missed = tkobj.tk_labelColor(self.frame_2, 3, 0, 20, "Color Missed:", "w", self.font, fg=config.COLOR_MISSED).getObj()
        self.label_released = tkobj.tk_labelColor(self.frame_2, 4, 0, 20, "Color Released:", "w", self.font, fg=config.COLOR_RELEASED).getObj()
        self.label_day_care = tkobj.tk_labelColor(self.frame_2, 5, 0, 20, "Color Day Car:", "w", self.font, fg=config.COLOR_DAY_CARE).getObj()
        self.label_pending = tkobj.tk_labelColor(self.frame_2, 6, 0, 20, "Color Pending:", "w", self.font, fg=config.COLOR_PENDING).getObj()
        tkobj.tk_Button(self.frame_2, 0, 1, 20, "Select Color Alive.", lambda : self.selectColor("COLORALIVE"))
        tkobj.tk_Button(self.frame_2, 1, 1, 20, "Select Color Dead.", lambda : self.selectColor("COLORDEAD"))
        tkobj.tk_Button(self.frame_2, 2, 1, 20, "Select Color Party.", lambda : self.selectColor("COLORPARTY"))
        tkobj.tk_Button(self.frame_2, 3, 1, 20, "Select Color Missed.", lambda : self.selectColor("COLORMISSED"))
        tkobj.tk_Button(self.frame_2, 4, 1, 20, "Select Color Released.", lambda : self.selectColor("COLORRELEASED"))
        tkobj.tk_Button(self.frame_2, 5, 1, 20, "Select Color Day Care.", lambda : self.selectColor("COLORDAYCARE"))
        tkobj.tk_Button(self.frame_2, 6, 1, 20, "Select Color Pending.", lambda : self.selectColor("COLORPENDING"))
        tkobj.tk_Radiobutton(self.frame_2, 0, 2, 20, "Alive", self.var_Color, "alive", self.updateImg)
        tkobj.tk_Radiobutton(self.frame_2, 1, 2, 20, "Dead", self.var_Color, "dead", self.updateImg)
        tkobj.tk_Radiobutton(self.frame_2, 2, 2, 20, "Party", self.var_Color, "party", self.updateImg)
        tkobj.tk_Radiobutton(self.frame_2, 3, 2, 20, "Missed", self.var_Color, "missed", self.updateImg)
        tkobj.tk_Radiobutton(self.frame_2, 4, 2, 20, "Released", self.var_Color, "released", self.updateImg)
        tkobj.tk_Radiobutton(self.frame_2, 5, 2, 20, "Day Care", self.var_Color, "day care", self.updateImg)
        tkobj.tk_Radiobutton(self.frame_2, 6, 2, 20, "Pending", self.var_Color, "pending", self.updateImg)

    # init_destination initializes input and labels for the image destination
    def init_destination(self):
        tkobj.tk_labelNoIO(self.frame_3, 0, 0, 20, "Party Dest:", "w", self.font)
        tkobj.tk_labelNoIO(self.frame_3, 1, 0, 20, "Other Pokemon Dest:", "w", self.font)
        tkobj.tk_Button(self.frame_3, 0, 1, 20, "Select Party Dest.", lambda : self.fileIO("PARTYDESTINATION", self.var_Party, filedialog.asksaveasfilename, ("PNG file", "*.png")))
        tkobj.tk_Button(self.frame_3, 1, 1, 20, "Select Other Pokemon Dest.", lambda : self.fileIO("OTHERMONSDESTINATION", self.var_OtherMons, filedialog.asksaveasfilename, ("PNG file", "*.png")))
        tkobj.tk_LabelIO(self.frame_3, 0, 2, 20, self.var_Party, "w", self.font)
        tkobj.tk_LabelIO(self.frame_3, 1, 2, 20, self.var_OtherMons, "w", self.font)

    # init_special initializes button and status label for default and start
    def init_special(self):
        tkobj.tk_Button(self.frame_4, 0, 0, 20, "Default", self.default)
        self.start = tkobj.tk_Button(self.frame_4, 1, 0, 20, "Start", lambda : self.startFunction(p)).getObj()
        self.label_status = tkobj.tk_labelColor(self.frame_4, 1, 1, 20, "idle", "w", self.font, "orange").getObj()

    # changeValue lambda for entry fields that maps input to configs
    # Args:
    #   config_ | str: string code mapping to a config
    #   var | StringVar: variable which stores new values
    def changeValue(self, config_, var):
        try:
            if config_ == "SPREAD" : config.SPREAD = var.get()
            if config_ == "SHEET" : config.SHEET = var.get()
            if config_ == "BLOCKSIZE" : config.BLOCKSIZE = int(var.get())
            if config_ == "PKMNSIZE" : config.PKMNSIZE = int(var.get())
            if config_ == "PKMNOFFSET_X" : config.PKMNOFFSET_X = int(var.get())
            if config_ == "PKMNOFFSET_Y" : config.PKMNOFFSET_Y = int(var.get())
            if config_ == "CIRCLEBONUS" : config.CIRCLEBONUS = int(var.get())
            if config_ == "TEXTOFFSET_X" : config.TEXTOFFSET_X = int(var.get())
            if config_ == "TEXTOFFSET_Y" : config.TEXTOFFSET_Y = int(var.get())
            if config_ == "FONTSIZE" : config.FONTSIZE = int(var.get())
            if config_ == "SPARKLEOFFSET" : config.SPARKLEOFFSET = int(var.get())
            self.updateImg()
            return True
        except:
            return False

    # upgradeImg redraws the preview picture
    def updateImg(self):    
        SAMPLE_MON = pokemon("0475-000","He Protect",self.var_Color.get(),"TRUE")
        temp_img =  asyncio.run(create_image([SAMPLE_MON], min=1))
        img2 = ImageTk.PhotoImage(temp_img)
        self.img_preview.configure( width=config.BLOCKSIZE, height=config.BLOCKSIZE,image=img2)
        self.img_preview.image = img2

    # fileIO opens the open / save file dialog 
    # Args:
    #   config_ | str: string code mapping to a config
    #   var | StringVar: variable which stores new values
    #   dialog | filedialog: decides what dialog is going to be used either Save or Open
    #   filetype | (str, str): major filetype which is filtered with the 2nd entry in the tupel
    def fileIO(self, config_, var, dialog, filetype):
        input = dialog(title = "Select file", filetypes=(filetype,("all files","*-*")))
        if input != "" and config_ == "FONT": configOS.FONT = input.replace("/",FOLDERSEP)
        if input != "" and config_ == "SPARKLESOURCE": configOS.SPARKLESOURCE = input.replace("/",FOLDERSEP)
        if input != "" and config_ == "PARTYDESTINATION": configOS.PARTYDESTINATION = input.replace("/",FOLDERSEP)
        if input != "" and config_ == "OTHERMONSDESTINATION": configOS.OTHERMONSDESTINATION = input.replace("/",FOLDERSEP)
        var.set(input.replace("/",FOLDERSEP).split(FOLDERSEP)[-1])

    # selectColor opens colorChooser dialog and reports the color to the correct config 
    # Args:
    #   config_ | str: string code mapping to a config
    def selectColor(self, config_):
        input = colorchooser.askcolor(title="Choose color")
        if input != (None, None) and config_ == "COLORALIVE" : 
            config.COLOR_ALIVE = input[1]
            self.label_alive.configure(fg=input[1])
            self.var_Color.set("alive")
        if input != (None, None) and config_ == "COLORDEAD" : 
            config.COLOR_DEAD = input[1]
            self.label_dead.configure(fg=input[1])
            self.var_Color.set("dead")
        if input != (None, None) and config_ == "COLORPARTY" : 
            config.COLOR_PARTY = input[1]
            self.label_party.configure(fg=input[1])
            self.var_Color.set("party")
        if input != (None, None) and config_ == "COLORMISSED" : 
            config.COLOR_MISSED = input[1]
            self.label_missed.configure(fg=input[1])
            self.var_Color.set("missed")
        if input != (None, None) and config_ == "COLORRELEASED" : 
            config.COLOR_RELEASED = input[1]
            self.label_released.configure(fg=input[1])
            self.var_Color.set("released")
        if input != (None, None) and config_ == "COLORDAYCARE" : 
            config.COLOR_DAY_CARE = input[1]
            self.label_day_care.configure(fg=input[1])
            self.var_Color.set("day care")
        if input != (None, None) and config_ == "COLORPENDING" : 
            config.COLOR_PENDING = input[1]
            self.label_pending.configure(fg=input[1])
            self.var_Color.set("pending")
        self.updateImg()

    # startFunction starts main routine, and swaps start-button and status-label, to stop-button and "running"
    # Args:
    #   process | Process: process which is going to be started
    def startFunction(self, process):
        asyncio.run(save_config())
        self.start.config(text = "stop", command=lambda : self.killFunction(p))
        process.start()
        self.label_status.config(text = "running", fg="green")
    
    # killFunction kills main routine, resets the process and swaps stop-button and status-label, to start-button and "idle"
    # Args:
    #    process | Process: process which is going to be started
    def killFunction(self, process):
        if process.is_alive():
            process.terminate()
        p = Process(target=initRunner, args=())
        self.start.config(text = "start", command=lambda : self.startFunction(p))
        self.label_status.config(text = "idle", fg="orange")

    # default loads default config, saves it as config, and call constructor
    def default(self):
        asyncio.run(load_configs(".data"+FOLDERSEP+"default.txt"))  
        asyncio.run(save_config())
        self.__init__(self.master)

    # __init__ constructs the NuzlockeParty Gui by calling the sub init functions
    # Args:
    #   master | tk.Tk: root level of gui 
    def __init__(self, master):
        asyncio.run(load_configs())        

        self.master = master
        master.title("Nuzlocke Party")
        
        self.font = ("bold", 10)  

        self.init_var()
        self.init_top_level()
        self.init_spreadsheet()
        self.init_preview()
        self.init_image()
        self.init_color()
        self.init_destination()
        self.init_special()

# main routine for NuzlockeParty
def main():
    try:
        root = tk.Tk()
        my_gui = NuzlockeParty(root)
        root.mainloop()
        if p.is_alive():
            p.terminate()
    except Exception as e:
        print(e)
        if p.is_alive():
            p.terminate()
        exit()

if __name__ == "__main__":
    # p global process to have it in scope in main but not create it in main to have scoped there
    p = Process(target=initRunner, args=())
    main()