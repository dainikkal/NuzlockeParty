import config 

class pokemon:
    # pokemon() contains all information about 1 pokemon shinyness will be added to id, 
    #   and status is converted to a color text
    # Args:
    #   id | string: pokedex-variation (0000-000)
    #   name | string: nickname of the pokemon
    #   status | string: status of the pokemon
    #   shiny | Bool: shinyness of the pokemon
    def __init__(self, id, name, status, shiny="FALSE"):
        self.id = id + ("-shiny" if shiny == "TRUE" else "")
        self.name = name
        if status == "alive"    : self.status = config.COLOR_ALIVE  
        if status == "day care" : self.status = config.COLOR_DAY_CARE 
        if status == "dead"     : self.status = config.COLOR_DEAD 
        if status == "missed"   : self.status = config.COLOR_MISSED 
        if status == "party"    : self.status = config.COLOR_PARTY  
        if status == "released" : self.status = config.COLOR_RELEASED
        if status == "pending"  : self.status = config.COLOR_PENDING 