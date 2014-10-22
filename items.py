# PLANE ITEMS -------------------------------------------------------------------------
item_toolkit = {
    "id": "toolkit",

    "name": "Multi-Toolkit",

    "description":
    """The Toolkit contains a knife, pliers, wire cutters. This could be useful for cutting wires which might get in your way!""",

    "mass": 300
}

def use_item_headtorch(player, locations, nice_print, Fore, Back):
    if not item_headtorch["on"]:
        item_headtorch["on"] = True
        nice_print("You turned on your headtorch. Everything looks a little bit brighter.", Fore.GREEN)
        return True
    else:
        item_headtorch["on"] = False
        nice_print("You turned off your headtorch. It's suddenly become a bit darker.", Fore.GREEN)
        return True


item_headtorch = {
    "id": "headtorch",

    "name": "headtorch",

    "description":
    """The headtorch can be used to see in dark areas. This could allow you to explore dark places such as caves.""",

    "mass": 150,

    "on": False,

    "use": use_item_headtorch
}

item_compass = {
    "id": "compass",

    "name": "compass",

    "description":
    """The compass will allow you to navigate directions, aiding you in your attempt for rescue.""",

    "mass": 250
}


# END-GAME ITEMS ------------------------------------------------------------------------------
def use_item_parachute(player, locations, nice_print, Fore, Back):
    if player["current_location"] == locations["Waterfall"]:
        nice_print("You parachute down to the ravine.", Fore.GREEN)
        player["current_location"] = locations["Ravine"]
        return True
    else:
        nice_print("There is no way to use that here.", Fore.RED)
        return False

item_parachute = {
    "id": "parachute",

    "name": "parachute",

    "description":
    """The parachute is still in good condition and could be used as a shelter.""",

    "mass": 1500,

    "use": use_item_parachute
}

item_combined_loaded_gun = {

    "id": "loaded_gun",

    "name": "a loaded gun",

    "description":
    """The gun is loaded and ready to fire with""",

    "mass": 850
}

item_gun = {
    "id": "gun",

    "name": "gun",

    "description":
    """The gun is a powerful weapon that can stop almost any foe.""",

    "mass": 700,

    "use_with": "bullets",

    "combined_item": item_combined_loaded_gun
}

item_bullets = {
    "id": "bullets",

    "name": "bullets",

    "description":
    """Powerful ammo for a gun""",

    "mass": 150,

    "use_with": "gun",

    "combined_item": item_combined_loaded_gun,
}

item_fire = {

    "id": "fire",

    "name": "fire",

    "description": "A large fire which can be used to signal for help.",

    "mass": 2300,

}

item_combined_petrol_pile = {

    "id": "petrolpile",

    "name": "pile of leaves and wood and petrol",

    "description": "Can be used with a spark to start a fire.",

    "mass": 2300,

    "use_with": "sparktool",

    "combined_item": item_fire,
}

item_combined_leaves_wood = {

    "id": "woodpile",

    "name": "pile of leaves and wood",

    "description": "Can be used to help start a fire.",

    "mass": 1100,

    "use_with": "petrol",

    "combined_item": item_combined_petrol_pile
}


item_petrol = {
    "id": "petrol",

    "name": "canister of petrol",

    "description":
    """A canister of petrol which could be used to aid in firemaking.""",

    "mass": 1200,

    "use_with": "woodpile",

    "combined_item": item_combined_petrol_pile
}

def use_item_sparktool(player, locations, nice_print, Fore, Back):
    if player["current_location"] == locations["Brush"] and not locations["Brush"]["fire"]:
        nice_print("You use the spark tool to set the barbed brush alight.", Fore.GREEN)
        locations["Brush"]["items"].append(item_machete)
        locations["Brush"]["fire"] = True
        locations["Brush"]["description"] = locations["Brush"]["description_alight"]
        return True
    else:
        nice_print("There is no way to use that here.", Fore.RED)
        return False

item_sparktool = {
    "id": "sparktool",

    "name": "spark tool",

    "description":
    """The spark tool which is made out of flint can be used to create sparks. When combined with other items it could produce fire.""",

    "mass": 250,

    "combined_item": item_fire,

    "use": use_item_sparktool,

    "use_with": item_combined_petrol_pile

}

item_wood = {
    "id": "wood",

    "name": "pile of wood",

    "description": "The wood pile can be used as fuel for a fire.",

    "mass": 1000,

    "use_with": "leaves",

    "combined_item": item_combined_leaves_wood
}

item_leaves = {
    "id": "leaves",

    "name": "pile of green leaves",

    "description":
    """An ordinary pile of green leaves.""",

    "mass": 100,

    "use_with": "wood",

    "combined_item": item_combined_leaves_wood
}


# SURVIVAL ITEMS -----------------------------------------------------------------------
item_medkit = {
    "id": "medkit",

    "name": "Med Kit",

    "description": "The medkit can be used to heal yourself.",

    "mass": 400
}

item_crisps = {
    "id": "crisps",

    "name": "bag of crisps",

    "description": "a bag of crisps will replenish your hunger.",

    "mass": 50
}

item_water = {
    "id": "water",

    "name": "bottle of water",

    "description": "Water can be used to replenish your thirst.",

    "mass": 150
}

item_chocolate = {
    "id": "chocolate",

    "name": "chocolate bar",

    "description": "A chocolate bar provides nutrition which replenishes your hunger.",

    "mass": 75
}

item_bandaids = {
    "id": "bandaids",

    "name": "band aid",

    "description": "Bandaids can be used to heal yourself.",

    "mass": 75
}
#ACCESS ITEMS -----------------------------------------------------------------------
def use_item_fireblanket(player, locations, nice_print, Fore, Back):
    if player["current_location"] == locations["Passage"]:
        nice_print("You use the fire blanket to put out the fire in the entrance to the cave.", Fore.GREEN)
        locations["Passage"]["description"] = locations["Passage"]["description_extinguished"]
        locations["Cave"]["fire"] = False
        player["inventory"].remove(item_fireblanket)
        player["inventory_weight"] -= item_fireblanket["mass"]
        return True
    else:
        nice_print("There is no way to use that here.", Fore.RED)
        return False

item_fireblanket = {
    "id": "fireblanket",

    "name": "fire blanket",

    "description":
    """The fire blanket will shield you from flames, allowing you to access areas blocked off from fire.""",

    "mass": 250,

    "use": use_item_fireblanket
}

def use_item_rope(player, locations, nice_print, Fore, Back):
    if player["current_location"] == locations["Hill"]:
        nice_print("You use the climbing rope to allow yourself to climb up to the flooded cave.", Fore.GREEN)
        player["current_location"]["exits"]["north"] = "Cave2"
        player["inventory"].remove(item_fireblanket)
        player["inventory_weight"] -= item_fireblanket["mass"]
        return True
    else:
        nice_print("There is no way to use that here.", Fore.RED)
        return False

item_rope = {
    "id": "rope",

    "name": "climbing rope",

    "description":
    """The rope can be used to climb around obstacles which could be blocking your path. """,

    "mass": 300,

    "use": use_item_rope
}


# WEAPONS ---------------------------------------------------------------------------
item_machete = {
    "id": "machete",

    "name": "rusty machete",

    "description": "The machete can be used to attack any animals or people who might try to attack you.",

    "mass": 1000
}

item_gun = {
    "id": "gun",

    "name": "gun",

    "description": "A gun can be used for protection against enemies",

    "mass": 2000
}

item_bullets = {
    "id": "bullets",

    "name": "bullets",

    "description": "Some extra bullets, just in case.",

    "mass": 750
}
