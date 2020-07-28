import tkinter as tk
import tkinter.ttk as ttk

# SuperClass
class tk_object:
    # Super Class
    # Args:
    #   tktype | tk.Obj: tkinter object name 
    #   tksuper | tk.Obj: parent 
    #   grid_row | int: row position in the grid from its parent 
    #   grid_col | int: col position in the grid from its parent 
    #   width | int: width of the object
    def __init__(self, tktype, tksuper, grid_row, grid_col, width=None):
        self.obj = tktype(tksuper)
        self.obj.grid(row=grid_row, column=grid_col)
        if width != None : self.obj.config(width=width)
    
    # getObj returns the object
    # Returns:
    #   obj | tk.Obj: returns the object which the class handled
    def getObj(self):
        return self.obj

# Frame
# Args:
#   tksuper | tk.Obj: parent 
#   grid_row | int: row position in the grid from its parent 
#   grid_col | int: col position in the grid from its parent 
#   sticky | str: direction it should obj will be sticking to
#   grid_rowspan | int: how many rows the frame should span over
class tk_frame(tk_object):
    def __init__(self, tksuper, grid_row, grid_col, sticky, grid_rowspan=None):
        super().__init__(tk.Frame, tksuper, grid_row, grid_col)
        self.obj.grid(sticky=sticky)
        if grid_rowspan != None : self.obj.grid(rowspan=grid_rowspan)

# Seperator
# Args:
#   tksuper | tk.Obj: parent 
#   grid_row | int: row position in the grid from its parent 
#   grid_col | int: col position in the grid from its parent 
#   sticky | str: direction it should obj will be sticking to
#   orient | str: orientation of the obj
class tk_seperator(tk_object):
    def __init__(self, tksuper, grid_row, grid_col, sticky, orient):
        super().__init__(ttk.Separator, tksuper, grid_row, grid_col)
        self.obj.config(orient=orient)
        self.obj.grid(sticky=sticky)

# Regular Label
# Args:
#   tksuper | tk.Obj: parent 
#   grid_row | int: row position in the grid from its parent 
#   grid_col | int: col position in the grid from its parent 
#   width | int: width of the object
#   text | str: name of the object
#   anchor | str: decides anchor direction
#   font | (str, int): decides font used for object
class tk_labelNoIO(tk_object):
    def __init__(self, tksuper, grid_row, grid_col, width, text, anchor, font):
        super().__init__(tk.Label, tksuper, grid_row, grid_col, width=width)
        self.obj.config(text=text, anchor=anchor, font=font)

# Label used for Image
# Args:
#   tksuper | tk.Obj: parent 
#   grid_row | int: row position in the grid from its parent 
#   grid_col | int: col position in the grid from its parent 
#   width | int: width of the object
#   height | int: height of the object
#   img | PhotoImage: image that should be represented
class tk_LabelIMG(tk_object):
    def __init__(self, tksuper, grid_row, grid_col, width, height, img):
        super().__init__(tk.Label, tksuper, grid_row, grid_col, width=width)
        self.obj.config(height=height, image=img)
    
# Label that gets its text changed
# Args:
#   tksuper | tk.Obj: parent 
#   grid_row | int: row position in the grid from its parent 
#   grid_col | int: col position in the grid from its parent 
#   width | int: width of the object
#   textvariable | StringVar: assigned stringvariable of the object
#   anchor | str: decides anchor direction
#   font | (str, int): decides font used for object
class tk_LabelIO(tk_object):
    def __init__(self, tksuper, grid_row, grid_col, width, textvariable, anchor, font):
        super().__init__(tk.Label, tksuper, grid_row, grid_col, width=width)
        self.obj.config(textvariable=textvariable, anchor=anchor, font=font)

# Colorized Label 
# Args:
#   tksuper | tk.Obj: parent 
#   grid_row | int: row position in the grid from its parent 
#   grid_col | int: col position in the grid from its parent 
#   width | int: width of the object
#   text | str: name of the object
#   anchor | str: decides anchor direction
#   font | (str, int): decides font used for object
#   fg | str: foreground color, color the text will have
class tk_labelColor(tk_object):
    def __init__(self, tksuper, grid_row, grid_col, width, text, anchor, font, fg):
        super().__init__(tk.Label, tksuper, grid_row, grid_col, width=width)
        self.obj.config(text=text, anchor=anchor, font=font, fg=fg)

# Entry
# Args:
#   tksuper | tk.Obj: parent 
#   grid_row | int: row position in the grid from its parent 
#   grid_col | int: col position in the grid from its parent 
#   width | int: width of the object
#   textvariable | StringVar: assigned stringvariable of the object
#   validate | str: decides when validatecommand should fire
#   validatecommand | function: function to be called when value changed
class tk_Entry(tk_object):
    def __init__(self, tksuper, grid_row, grid_col, width, textvariable, validate, validatecommand):
        super().__init__(tk.Entry, tksuper, grid_row, grid_col, width=width)
        self.obj.config(textvariable=textvariable, validate=validate, validatecommand=validatecommand)

# Button
# Args:
#   tksuper | tk.Obj: parent 
#   grid_row | int: row position in the grid from its parent 
#   grid_col | int: col position in the grid from its parent 
#   width | int: width of the object
#   text | str: name of the object
#   command | function: function to be called when changed
class tk_Button(tk_object):
    def __init__(self, tksuper, grid_row, grid_col, width, text, command):
        super().__init__(tk.Button, tksuper, grid_row, grid_col, width=width)
        self.obj.config(text=text, command=command)
    
# Radiobutton
# Args:
#   tksuper | tk.Obj: parent 
#   grid_row | int: row position in the grid from its parent 
#   grid_col | int: col position in the grid from its parent 
#   width | int: width of the object
#   text | str: name of the object
#   variable | StringVar: assigned variable of the object
#   value | str: value the obj represents
#   command | function: function to be called when changed
class tk_Radiobutton(tk_object):
    def __init__(self, tksuper, grid_row, grid_col, width, text, variable, value, command):
        super().__init__(tk.Radiobutton, tksuper, grid_row, grid_col, width=width)
        self.obj.config(text=text, variable=variable, value=value, command=command)

            