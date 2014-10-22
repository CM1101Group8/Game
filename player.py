from items import *
from map import locations

player = {
    "health": 100,
    "inventory": [item_toolkit, item_headtorch, item_compass, item_wood, item_petrol, item_leaves, item_sparktool, item_machete],
    "inventory_weight": 950,
    "current_location": locations["Cliffs"],
    "previous_location": locations["Plane"]
}
