import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, colorchooser
from PIL import Image, ImageTk
import asyncio
from functools import partial

import tk_object as tkobj
from pokemon_class import pokemon
from imagecreation import create_image
from multiprocessing import Process
from config_file_management import load_configs, save_config
from main import runner

import platform
import config
if platform.system() == 'Linux':
    import config_linux as configOS
    FOLDERSEP = "/"
elif platform.system() == 'Windows':
    import config_win as configOS
    FOLDERSEP = "\\"

if __name__ == "__main__":
    try: 
        asyncio.run(load_configs())
        #subprocess to start later
        p = Process(target=runner, args=())
            
        root = tk.Tk()
        root.title("Nuzlocke Party Config")

        #Changing Variables
        var_Spread = tk.StringVar(value=config.SPREAD)
        var_Sheet = tk.StringVar(value=config.SHEET)
        var_BlockSize = tk.StringVar(value=config.BLOCKSIZE)
        var_PkmnSize = tk.StringVar(value=config.PKMNSIZE)
        var_PkmnOffsetX = tk.StringVar(value=config.PKMNOFFSET_X)
        var_PkmnOffsetY = tk.StringVar(value=config.PKMNOFFSET_Y)
        var_CircleBonus = tk.StringVar(value=config.CIRCLEBONUS)
        var_TextOffsetX = tk.StringVar(value=config.TEXTOFFSET_X)
        var_TextOffsetY = tk.StringVar(value=config.TEXTOFFSET_Y)
        var_SparkleOffset = tk.StringVar(value=config.SPARKLEOFFSET)
        var_FontSize = tk.StringVar(value=config.FONTSIZE)
        varFont = tk.StringVar(value=configOS.FONT.split(FOLDERSEP)[-1])
        var_Sparkle = tk.StringVar(value=configOS.SPARKLESOURCE.split(FOLDERSEP)[-1])
        var_Party = tk.StringVar(value=configOS.PARTYDESTINATION.split(FOLDERSEP)[-1])
        var_OtherMons = tk.StringVar(value=configOS.OTHERMONSDESTINATION.split(FOLDERSEP)[-1])
        var_Color = tk.StringVar(value="party")

        #changeValue
        def changeValue(config_, var):
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
                updateImg()
                return True
            except:
                return False

        def updateImg():    
            SAMPLE_MON = pokemon("0475-000","He Protect",var_Color.get(),"TRUE")
            temp_img =  asyncio.run(create_image([SAMPLE_MON], min=1))
            img2 = ImageTk.PhotoImage(temp_img)
            img_preview.configure( width=config.BLOCKSIZE, height=config.BLOCKSIZE,image=img2)
            img_preview.image = img2

        def fileIO(config_, var, dialog, filetype):
            input = dialog(title = "Select file", filetypes=(filetype,("all files","*-*")))
            if input != "" and config_ == "FONT": configOS.FONT = input.replace("/",FOLDERSEP)
            if input != "" and config_ == "SPARKLESOURCE": configOS.SPARKLESOURCE = input.replace("/",FOLDERSEP)
            if input != "" and config_ == "PARTYDESTINATION": configOS.PARTYDESTINATION = input.replace("/",FOLDERSEP)
            if input != "" and config_ == "OTHERMONSDESTINATION": configOS.OTHERMONSDESTINATION = input.replace("/",FOLDERSEP)
            var.set(input.replace("/",FOLDERSEP).split(FOLDERSEP)[-1])

        def selectColor(config_):
            input = colorchooser.askcolor(title="Choose color")
            if input != (None, None) and config_ == "COLORALIVE" : 
                config.COLOR_ALIVE = input[1]
                label_alive.configure(fg=input[1])
                var_Color.set("alive")
            if input != (None, None) and config_ == "COLORDEAD" : 
                config.COLOR_DEAD = input[1]
                label_dead.configure(fg=input[1])
                var_Color.set("dead")
            if input != (None, None) and config_ == "COLORPARTY" : 
                config.COLOR_PARTY = input[1]
                label_party.configure(fg=input[1])
                var_Color.set("party")
            if input != (None, None) and config_ == "COLORMISSED" : 
                config.COLOR_MISSED = input[1]
                label_missed.configure(fg=input[1])
                var_Color.set("missed")
            if input != (None, None) and config_ == "COLORRELEASED" : 
                config.COLOR_RELEASED = input[1]
                label_released.configure(fg=input[1])
                var_Color.set("released")
            if input != (None, None) and config_ == "COLORDAYCARE" : 
                config.COLOR_DAY_CARE = input[1]
                label_day_care.configure(fg=input[1])
                var_Color.set("day care")
            if input != (None, None) and config_ == "COLORPENDING" : 
                config.COLOR_PENDING = input[1]
                label_pending.configure(fg=input[1])
                var_Color.set("pending")
            updateImg()

        def startOperation(process):
            asyncio.run(save_config())
            start.config(text = "stop", command=lambda : joinOperation(p) )
            process.start()
        
        def joinOperation(process):
            if process.is_alive():
                process.terminate()
            p = Process(target=runner, args=())
            start.config(text = "start", command=lambda : startOperation(p) )

        def default():
            asyncio.run(load_configs(".data"+FOLDERSEP+"default.txt"))  
            asyncio.run(save_config())

        #image pregen
        temp_img = Image.new("RGBA",(config.BLOCKSIZE,config.BLOCKSIZE),"black")
        img = ImageTk.PhotoImage(temp_img)
        font = ("bold", 10)

        #frames
        frame_0 = tkobj.tk_frame(root, 0, 0, "w").getObj()
        tkobj.tk_seperator(root, 1, 0, "ew", tk.HORIZONTAL)
        frame_1 = tkobj.tk_frame(root, 2, 0, "w").getObj()
        tkobj.tk_seperator(root, 3, 0, "ew", tk.HORIZONTAL)
        frame_2 = tkobj.tk_frame(root, 4, 0, "w").getObj()
        tkobj.tk_seperator(root, 5, 0, "ew", tk.HORIZONTAL)
        frame_3 = tkobj.tk_frame(root, 6, 0, "w").getObj()
        tkobj.tk_seperator(root, 7, 0, "ew", tk.HORIZONTAL)
        frame_4 = tkobj.tk_frame(root, 8, 0, "w").getObj()

        #spreadsheet
        tkobj.tk_labelNoIO(frame_0, 0, 0, 20, "Spreadsheet name:", "w", font)
        tkobj.tk_labelNoIO(frame_0, 1, 0, 20, "Sheet page name:", "w", font)
        tkobj.tk_Entry(frame_0, 0, 1, 20, var_Spread, "focusout", lambda : changeValue("SPREAD", var_Spread))
        tkobj.tk_Entry(frame_0, 1, 1, 20, var_Sheet, "focusout", lambda : changeValue("SHEET", var_Sheet))

        #image preview
        frame_preview = tkobj.tk_frame(frame_1, 0, 2, "e", 6).getObj()
        img_preview = tkobj.tk_LabelIMG(frame_preview, 0, 0, config.BLOCKSIZE, config.BLOCKSIZE, img).getObj()

        #image settings
        tkobj.tk_labelNoIO(frame_1, 0, 0, 20, "Blocksize:", "w", font)
        tkobj.tk_labelNoIO(frame_1, 1, 0, 20, "Pokemon Size:", "w", font)
        tkobj.tk_labelNoIO(frame_1, 2, 0, 20, "Pokemon Offset(X):", "w", font)
        tkobj.tk_labelNoIO(frame_1, 3, 0, 20, "Pokemon Offset(Y):", "w", font)
        tkobj.tk_labelNoIO(frame_1, 4, 0, 20, "Circle Extension:", "w", font)
        tkobj.tk_labelNoIO(frame_1, 5, 0, 20, "Text Offset(X):", "w", font)
        tkobj.tk_labelNoIO(frame_1, 6, 0, 20, "Text Offset(Y):", "w", font)
        tkobj.tk_labelNoIO(frame_1, 7, 0, 20, "Font: ", "w", font)
        tkobj.tk_labelNoIO(frame_1, 8, 0, 20, "Font Size:", "w", font)
        tkobj.tk_labelNoIO(frame_1, 9, 0, 20, "Sparkle: ", "w", font)
        tkobj.tk_labelNoIO(frame_1, 10, 0, 20, "Sparkle Offset:", "w", font)
        tkobj.tk_Entry(frame_1, 0, 1, 20, var_BlockSize, "focusout", lambda : changeValue("BLOCKSIZE", var_BlockSize))
        tkobj.tk_Entry(frame_1, 1, 1, 20, var_PkmnSize, "focusout", lambda : changeValue("PKMNSIZE", var_PkmnSize))
        tkobj.tk_Entry(frame_1, 2, 1, 20, var_PkmnOffsetX, "focusout", lambda : changeValue("PKMNOFFSET_X", var_PkmnOffsetX))
        tkobj.tk_Entry(frame_1, 3, 1, 20, var_PkmnOffsetY, "focusout", lambda : changeValue("PKMNOFFSET_Y", var_PkmnOffsetY))
        tkobj.tk_Entry(frame_1, 4, 1, 20, var_CircleBonus, "focusout", lambda : changeValue("CIRCLEBONUS", var_CircleBonus))
        tkobj.tk_Entry(frame_1, 5, 1, 20, var_TextOffsetX, "focusout", lambda : changeValue("TEXTOFFSET_X", var_TextOffsetX))
        tkobj.tk_Entry(frame_1, 6, 1, 20, var_TextOffsetY, "focusout", lambda : changeValue("TEXTOFFSET_Y", var_TextOffsetY))
        tkobj.tk_Button(frame_1, 7, 1, 20, "Select Fontfile", lambda : fileIO("FONT", varFont, filedialog.askopenfilename, ("font file", "*.ttf")))
        tkobj.tk_Entry(frame_1, 8, 1, 20, var_FontSize, "focusout", lambda : changeValue("FONTSIZE", var_FontSize))
        tkobj.tk_Button(frame_1, 9, 1, 20, "Select Sparklefile", lambda : fileIO("SPARKLESOURCE", var_Sparkle, filedialog.askopenfilename, ("PNG file", "*.png")))
        tkobj.tk_Entry(frame_1, 10, 1, 20, var_SparkleOffset, "focusout", lambda : changeValue("SPARKLEOFFSET", var_SparkleOffset))
        tkobj.tk_LabelIO(frame_1, 7, 2, 20, varFont, "w", font)
        tkobj.tk_LabelIO(frame_1, 9, 2, 20, var_Sparkle, "w", font)

        #color)
        label_alive = tkobj.tk_labelColor(frame_2, 0, 0, 20, "Color Alive:", "w", font, fg=config.COLOR_ALIVE).getObj()
        label_dead = tkobj.tk_labelColor(frame_2, 1, 0, 20, "Color Dead:", "w", font, fg=config.COLOR_DEAD).getObj()
        label_party = tkobj.tk_labelColor(frame_2, 2, 0, 20, "Color Party:", "w", font, fg=config.COLOR_PARTY).getObj()
        label_missed = tkobj.tk_labelColor(frame_2, 3, 0, 20, "Color Missed:", "w", font, fg=config.COLOR_MISSED).getObj()
        label_released = tkobj.tk_labelColor(frame_2, 4, 0, 20, "Color Released:", "w", font, fg=config.COLOR_RELEASED).getObj()
        label_day_care = tkobj.tk_labelColor(frame_2, 5, 0, 20, "Color Day Car:", "w", font, fg=config.COLOR_DAY_CARE).getObj()
        label_pending = tkobj.tk_labelColor(frame_2, 6, 0, 20, "Color Pending:", "w", font, fg=config.COLOR_PENDING).getObj()
        tkobj.tk_Button(frame_2, 0, 1, 20, "Select Color Alive.", lambda : selectColor("COLORALIVE"))
        tkobj.tk_Button(frame_2, 1, 1, 20, "Select Color Dead.", lambda : selectColor("COLORDEAD"))
        tkobj.tk_Button(frame_2, 2, 1, 20, "Select Color Party.", lambda : selectColor("COLORPARTY"))
        tkobj.tk_Button(frame_2, 3, 1, 20, "Select Color Missed.", lambda : selectColor("COLORMISSED"))
        tkobj.tk_Button(frame_2, 4, 1, 20, "Select Color Released.", lambda : selectColor("COLORRELEASED"))
        tkobj.tk_Button(frame_2, 5, 1, 20, "Select Color Day Care.", lambda : selectColor("COLORDAYCARE"))
        tkobj.tk_Button(frame_2, 6, 1, 20, "Select Color Pending.", lambda : selectColor("COLORPENDING"))
        tkobj.tk_Radiobutton(frame_2, 0, 2, 20, "Alive", var_Color, "alive", updateImg)
        tkobj.tk_Radiobutton(frame_2, 1, 2, 20, "Dead", var_Color, "dead", updateImg)
        tkobj.tk_Radiobutton(frame_2, 2, 2, 20, "Party", var_Color, "party", updateImg)
        tkobj.tk_Radiobutton(frame_2, 3, 2, 20, "Missed", var_Color, "missed", updateImg)
        tkobj.tk_Radiobutton(frame_2, 4, 2, 20, "Released", var_Color, "released", updateImg)
        tkobj.tk_Radiobutton(frame_2, 5, 2, 20, "Day Care", var_Color, "day care", updateImg)
        tkobj.tk_Radiobutton(frame_2, 6, 2, 20, "Pending", var_Color, "pending", updateImg)

        #Destination
        tkobj.tk_labelNoIO(frame_3, 0, 0, 20, "Party Dest:", "w", font)
        tkobj.tk_labelNoIO(frame_3, 1, 0, 20, "Other Pokemon Dest:", "w", font)
        tkobj.tk_Button(frame_3, 0, 1, 20, "Select Party Dest.", lambda : fileIO("PARTYDESTINATION", var_Party, filedialog.asksaveasfilename, ("PNG file", "*.png")))
        tkobj.tk_Button(frame_3, 1, 1, 20, "Select Other Pokemon Dest.", lambda : fileIO("OTHERMONSDESTINATION", var_OtherMons, filedialog.asksaveasfilename, ("PNG file", "*.png")))
        tkobj.tk_LabelIO(frame_3, 0, 2, 20, var_Party, "w", font)
        tkobj.tk_LabelIO(frame_3, 1, 2, 20, var_OtherMons, "w", font)

        start = tkobj.tk_Button(frame_4, 0, 0, 60, "Start", lambda : startOperation(p)).getObj()
        tkobj.tk_Button(frame_4, 1, 0, 60, "Default", default)

        root.mainloop()
        if p.is_alive():
            p.terminate()
    except:
        exit()