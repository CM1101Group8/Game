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

    "exits": {"west": "MON1", "north": "MON2", "east": "MON3"},

    "items": [],

    "visited": False
}

location_mon1 = {
    "name": "Middle of Nowhere",

    "description":
    """
    TODO
    """,

    "exits": {"east": "Plane", "north": "Ravine", "west": "Rockside"},

    "items": [],

    "visited": False
}

location_mon2 = {
    "name": "Middle of Nowhere",

    "description":
    """
    TODO
    """,

    "exits": {"north": "HOF", "south": "Plane", "west": "Ravine", "east": "Woods"},

    "items": [],

    "visited": False
}

location_mon3 = {
    "name": "Middle of Nowhere",

    "description":
    """
    TODO
    """,

    "exits": {"west": "Plane", "east": "Beach", "north": "Woods"},

    "items": [],

    "visited": False
}

location_hof = {
    "name": "Heart of the Forest",

    "description":
    """
    TODO
    """,

    "exits": {"south": "MON2", "north": "Passage"},

    "items": [item_wood],

    "visited": False
}

location_ravine = {
    "name": "Ravine",

    "description":
    """
    TODO
    """,

    "exits": {"south": "MON1", "west": "Brush", "east": "MON2", },

    "items": [],

    "visited": False
}

location_brush = {
    "name": "Barbed Brush",

    "description":
    """
    TODO
    """,

    "exits": {"east": "Ravine"},

    "items": [item_machete, item_wood],

    "visited": False
}

location_rockside = {
    "name": "Rockside",

    "description":
    """
    TODO
    """,

    "exits": {"east": "MON1"},

    "items": [item_sparktool],

    "visited": False
}

location_woods = {
    "name": "Dry Woods",

    "description":
    """
    TODO
    """,

    "exits": {"west": "MON2", "east": "Cliffs", "south": "MON3"},

    "items": [item_wood],

    "visited": False
}

location_cliffs = {
    "name": "Cliffs",

    "description":
    """
    TODO
    """,

    "exits": {"west": "Woods"},

    "items": [],

    "visited": False
}

location_beach = {
    "name": "Beach",

    "description":
    """
    TODO
    """,

    "exits": {"west": "MON3"},

    "items": [item_medkit, item_crisps],

    "visited": False
}

location_passage = {
    "name": "Dark Passage",

    "description":
    """
    TODO
    """,

    "exits": {"south": "HOF"},

    "items": [],

    "visited": False
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
