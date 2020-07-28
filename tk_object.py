import tkinter as tk
import tkinter.ttk as ttk
class tk_object:
    def __init__(self, tktype, tksuper, grid_row, grid_col, width=None):
        self.obj = tktype(tksuper)
        self.obj.grid(row=grid_row, column=grid_col)
        if width != None : self.obj.config(width=width)
        
    def getObj(self):
        return self.obj

#Frame
class tk_frame(tk_object):
    def __init__(self, tksuper, grid_row, grid_col, sticky, grid_rowspan=None):
        super().__init__(tk.Frame, tksuper, grid_row, grid_col)
        self.obj.grid(sticky=sticky)
        if grid_rowspan != None : self.obj.grid(rowspan=grid_rowspan)

#Seperator
class tk_seperator(tk_object):
    def __init__(self, tksuper, grid_row, grid_col, sticky, orient):
        super().__init__(ttk.Separator, tksuper, grid_row, grid_col)
        self.obj.config(orient=orient)
        self.obj.grid(sticky=sticky)

#NoIO Label
class tk_labelNoIO(tk_object):
    def __init__(self, tksuper, grid_row, grid_col, width, text, anchor, font):
        super().__init__(tk.Label, tksuper, grid_row, grid_col, width=width)
        self.obj.config(text=text, anchor=anchor, font=font)

#Label Img
class tk_LabelIMG(tk_object):
    def __init__(self, tksuper, grid_row, grid_col, width, height, img):
        super().__init__(tk.Label, tksuper, grid_row, grid_col, width=width)
        self.obj.config(height=height, image=img)
    
#IO Label
class tk_LabelIO(tk_object):
    def __init__(self, tksuper, grid_row, grid_col, width, textvariable, anchor, font):
        super().__init__(tk.Label, tksuper, grid_row, grid_col, width=width)
        self.obj.config(textvariable=textvariable, anchor=anchor, font=font)

class tk_labelColor(tk_object):
    def __init__(self, tksuper, grid_row, grid_col, width, text, anchor, font, fg):
        super().__init__(tk.Label, tksuper, grid_row, grid_col, width=width)
        self.obj.config(text=text, anchor=anchor, font=font, fg=fg)

#Entry
class tk_Entry(tk_object):
    def __init__(self, tksuper, grid_row, grid_col, width, textvariable, validate, validatecommand):
        super().__init__(tk.Entry, tksuper, grid_row, grid_col, width=width)
        self.obj.config(textvariable=textvariable, validate=validate, validatecommand=validatecommand)
    
#Button
class tk_Button(tk_object):
    def __init__(self, tksuper, grid_row, grid_col, width, text, command):
        super().__init__(tk.Button, tksuper, grid_row, grid_col, width=width)
        self.obj.config(text=text, command=command)
    
#Radiobutton
class tk_Radiobutton(tk_object):
    def __init__(self, tksuper, grid_row, grid_col, width, text, variable, value, command):
        super().__init__(tk.Radiobutton, tksuper, grid_row, grid_col, width=width)
        self.obj.config(text=text, variable=variable, value=value, command=command)

            