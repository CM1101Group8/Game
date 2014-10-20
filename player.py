from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]

inventory_weight = 2070

# Start game at the reception
current_room = rooms["Reception"]

player = {"name":"Group 8", "health":100, "experience": 100,"inventory":inventory}
