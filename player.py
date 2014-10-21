from items import *
from map import locations

player = {
    "health": 100,
    "experience": 100,
    "inventory": [item_toolkit, item_headtorch, item_compass],
    "inventory_weight": 950,
    "current_location": locations["Plane"],
    "previous_location": locations["Plane"]
}
