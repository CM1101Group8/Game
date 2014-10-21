from items import *

location_plane = {
    "name": "Plane",

    "description":
    """
    The plane ends up crash landing into a forest on an island,
    killing all passengers & crew on board, apart from YOU,
    as far as you're aware anyway. Upon waking, it seems you
    do not know where the plane took off from, where it is,
    and where it was going; amnesia it seems. Most of the
    supplies were either lost when the plane was in freefall,
    taken considerable damage, been burnt out by the fires,
    or simply lost amongst the destruction and rubble.
    """,

    "exits": {"east": "MON1", "north": "MON2", "west": "MON3"},

    "items": []
}

location_mon1 = {
    "name": "Middle of Nowhere",

    "description": 
    """
    You find yourself in the middle of nowhere. There is nothing 
    here except the burning plane you just escaped from. You 
    have no choice but to move on.
    """,

    "exits": {"west": "Plane", "north": "Ravine", "west": "Rockside"},

    "items": []
}

location_mon2 = {
    "name": "Middle of Nowhere",

    "description":
    """
    You find yourself in the middle of nowhere. There is nothing
    here except the burning plane you just escaped from. You
    have no choice but to move on.
    """,

    "exits": {"north": "HOF", "south": "Plane", "west": "Ravine", "east": "Woods"},

    "items": []
}

location_mon3 = {
    "name": "Middle of Nowhere",

    "description":
    """
    You find yourself in the middle of nowhere. You find
    the charred corpses of Owen and Beru Lars. They have
    nothing to help you survive, it is best to move on.
    """,

    "exits": {"west": "Plane", "east": "Beach", "north": "Woods"},

    "items": []
}

location_hof = {
    "name": "Heart of the Forest",

    "description":
    """
    You are now in the heart of the forest. Without
    your head torch, you cannot see anything. It is 
    no use trying to look at your compass. Surrounded 
    by the darkness, you begin to feel light-headed, 
    and anxiously turn your head and trying to sharpen 
    your hearing; you fear something is approaching.
    """,

    "exits": {"south": "MON2", "north": "Passage"},

    "items": [item_wood]
}

location_ravine = {
    "name": "Ravine",

    "description":
    """
    You are now at the ravine. It is peaceful here, 
    and there is a pile of green leaves on the floor. 
    It is possible those may be useful.
    """,

    "exits": {"south": "MON1", "west": "Brush", "east": "MON2", },

    "items": []
}

location_brush = {
    "name": "Barbed Brush",

    "description":
    """
    You’ve made it to some barbed brush. It looks
    spikey and there is the corpse of Danny Trejo. 
    It makes you want to turn around, but there is 
    some wood and a rusty machete there.
    """,

    "exits": {"east": "Ravine"},

    "items": [item_machete, item_wood]
}

location_rockside = {
    "name": "Rockside",

    "description":
    """
    You are now at the rockside. Amongst all 
    the rocks there is a scary but satisfying sight: 
    Bear Grylls’ corpse. At least you out-survived him. 
    There appears to be some sort of tool on his body.
    """,

    "exits": {"east": "MON1"},

    "items": [item_sparktool]
}

location_woods = {
    "name": "Dry Woods",

    "description":
    """
    You are in the woods. It is dingy and 
    very dry, much like the pile of wood on the floor.
    
    """,

    "exits": {"west": "MON2", "east": "Cliffs", "south": "MON3"},

    "items": [item_wood]
}

location_cliffs = {
    "name": "Cliffs",

    "description":
    """
    You’re at the cliffs. It’s high up, and there is 
    some climbing rope. You have a great view of…. 
    CRAZY ANGRY KIRILL TRYING TO KILL YOU FOR YOUR POOR TEST SCORE. 
    """,

    "exits": {"west": "Woods"},

    "items": []
}

location_beach = {
    "name": "Beach",

    "description":
    """
    You’re on a nice island beach. It’s pleasant... 
    until you remember you’re stranded on an island 
    trying not to die. There’s a medi-kit and a bag of 
    crisps. It’s your lucky day... ish.
    """,

    "exits": {"west": "MON3"},

    "items": [item_medkit, item_crisps]
}

location_passage = {
    "name": "Dark Passage",

    "description":
    """
    TODO
    """,

    "exits": {"south": "HOF"},

    "items": []
}

locations = {
    "Plane": location_plane,
    "MON1": location_mon1,
    "MON2": location_mon2,
    "MON3": location_mon3,
    "HOF": location_hof,
    "Ravine": location_ravine,
    "Brush": location_brush,
    "Rockside": location_rockside,
    "Woods": location_woods,
    "Cliffs": location_cliffs,
    "Beach": location_beach,
    "Passage": location_passage
}
