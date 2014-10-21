# PLANE ITEMS -------------------------------------------------------------------------
item_toolkit = {
    "id": "toolkit",

    "name": "a Multi-Toolkit",

    "description":
    """The Toolkit contains a knife, pliers, wire cutters. This could be useful for cutting wires which might get in your way!""",

    "mass": 300
}


item_headtorch = {
    "id": "headtorch",

    "name": "a headtorch",

    "description":
    """The headtorch can be used to see in dark areas. This could allow you to explore dark places such as caves.""",

    "mass": 150
}

item_compass = {
    "id": "compass",

    "name": "a compass",

    "description":
    """The compass will allow you to navigate directions, aiding you in your attempt for rescue.""",

    "mass": 250
}


# END-GAME ITEMS ------------------------------------------------------------------------------
item_parachute = {
    "id": "parachute",

    "name": "a parachute",

    "description":
    """The parachute is still in good condition and could be used as a shelter.""",

    "mass": 1500
}


item_combined_leaves_wood = {
    
    "id": "",

    "name": "a pile of leaves and wood",

    "description": "Can be used to help start a fire.",

    "mass": 1100,
}

item_combined_petrol_pile = {

    "id": "",

    "name": "a pile of leaves and wood and petrol",

    "description": "Can be used with a spark to start a fire.",

    "mass": 2300,
    
}

item_fire = {

    "id": "",

    "name": "a fire",

    "description": "A large fire which can be used to signal for help.",

    "mass": 2300,
    
}


item_petrol = {
    "id": "petrol",

    "name": "a canister of petrol",

    "description":
    """A canister of petrol which could be used to aid in firemaking.""",

    "mass": 1200,

    "combined_item": item_combined_petrol_pile
}

item_sparktool = {
    "id": "sparktool",

    "name": "a spark tool",

    "description":
    """The spark tool which is made out of flint can be used to create sparks. When combined with other items it could produce fire.""",

    "mass": 250,

    "combined_item": item_fire
}

item_wood = {
    "id": "wood",

    "name": "a pile of wood",

    "description": "The wood pile can be used as fuel for a fire.",

    "mass": 1000, 

    "combined_item": item_combined_leaves_wood
}

item_leaves = {
    "id": "leaves",

    "name": "a pile of leaves",

    "description":
    """An ordinary pile of leaves.""",

    "mass": 100,

    "combined_item": item_combined_leaves_wood
}


item_combinations = {

    "wood": item_leaves,

    "petrol": item_combined_leaves_wood,

    "sparktool": item_combined_petrol_pile,

    "leaves": item_wood
}

# SURVIVAL ITEMS -----------------------------------------------------------------------
item_medkit = {
    "id": "medkit",

    "name": "a Med Kit",

    "description": "The medkit can be used to heal yourself.",

    "mass": 400 
}

item_crisps = {
    "id": "crisps",

    "name": "a bag of crisps",

    "description": "a bag of crisps will replenish your hunger.",

    "mass": 50
}

item_water = {
    "id": "water",

    "name": "a bottle of water",

    "description": "Water can be used to replenish your thirst.",

    "mass": 150
}

item_chocolate = {
    "id": "chocolate",

    "name": "a chocolate bar",

    "description": "A chocolate bar provides nutrition which replenishes your hunger.",

    "mass": 75
}

item_bandaids = {
    "id": "bandaids",

    "name": "some band aids",

    "description": "Bandaids can be used to heal yourself.",

    "mass": 75
}
#ACCESS ITEMS -----------------------------------------------------------------------
item_fireblanket = {
    "id": "fireblanket",

    "name": "a fire blanket",

    "description":
    """The fire blanket will shield you from flames, allowing you to access areas blocked off from fire.""",

    "mass": 250
}

item_rope = {
    "id": "rope",

    "name": "climbimg rope",
    
    "description":
    """ The rope can be used to climb around obstacles which could be blocking your path. """,

    "mass": 300
}


# WEAPONS ---------------------------------------------------------------------------
item_machete = {
    "id": "machete",

    "name": "a rusty machete",

    "description": "The machete can be used to attack any animals or people who might try to attack you.",

    "mass": 1000
}
