# SHEET on which gsheet spreadsheet
SPREAD = "DBs Nuzlockes"
# SHEET on which gsheet sheet
SHEET = "TESTING"

# BLOCKSIZE of a block which is from image top to down, includes pokemon circle and name.
BLOCKSIZE = 150

# PKMNSIZE size of picture of the pokemon model.
PKMNSIZE = 90
# PKMNOFFSET from the left of the Block to the pokemon
PKMNOFFSET_X = int((BLOCKSIZE - PKMNSIZE)/ 2)
# PKMNOFFSET from the top of the Block to the pokemon
PKMNOFFSET_Y = 15

# CIRCLEBONUS how much bigger the circle is than PKMNSIZE
CIRCLEBONUS = 5

# TEXTOFFSET from the left of the Block to the name
TEXTOFFSET_X = PKMNOFFSET_X
# TEXTOFFSET from the top of the Block to the name
TEXTOFFSET_Y = PKMNSIZE + PKMNOFFSET_Y + 5

# FONTSIZE Size of Font
FONTSIZE = 27

# SPARKLEOFFSET from the top left corner of the pkmn area in box X and Y 
SPARKLEOFFSET = int(PKMNSIZE *2 /3)

# QUALITY that should be used when saving a picture
QUALITY = 100

# COLORS_XXX color text code for the specific status
COLOR_ALIVE='orange'
COLOR_DEAD='red'
COLOR_PARTY='green'
COLOR_MISSED='grey'
COLOR_RELEASED='black'
COLOR_DAY_CARE='pink'
COLOR_PENDING='blue'
