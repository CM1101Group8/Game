from items import *

location_plane = {
    "name": "Plane",

    "description":
    """
    TODO
    """,

    "exits": {"east": "MON1", "north": "MON2", "west": "MON3"},

    "items": []
}

location_mon1 = {
    "name": "Middle of Nowhere",

    "description":
    """
    TODO
    """,

    "exits": {"west": "Plane", "north": "Ravine", "west": "Rockside"},

    "items": []
}

location_mon2 = {
    "name": "Middle of Nowhere",

    "description":
    """
    TODO
    """,

    "exits": {"north": "HOF", "south": "Plane", "west": "Ravine", "east": "Woods"},

    "items": []
}

location_mon3 = {
    "name": "Middle of Nowhere",

    "description":
    """
    TODO
    """,

    "exits": {"west": "Plane", "east": "Beach", "north": "Woods"},

    "items": []
}

location_hof = {
    "name": "Heart of the Forest",

    "description":
    """
    TODO
    """,

    "exits": {"south": "MON2", "north": "Passage"},

    "items": [item_wood]
}

location_ravine = {
    "name": "Ravine",

    "description":
    """
    TODO
    """,

    "exits": {"south": "MON1", "west": "Brush", "east": "MON2", },

    "items": []
}

location_brush = {
    "name": "Barbed Brush",

    "description":
    """
    TODO
    """,

    "exits": {"east": "Ravine"},

    "items": [item_machete, item_wood]
}

location_rockside = {
    "name": "Rockside",

    "description":
    """
    TODO
    """,

    "exits": {"east": "MON1"},

    "items": [item_sparktool]
}

location_woods = {
    "name": "Dry Woods",

    "description":
    """
    TODO
    """,

    "exits": {"west": "MON2", "east": "Cliffs", "south": "MON3"},

    "items": [item_wood]
}

location_cliffs = {
    "name": "Cliffs",

    "description":
    """
    TODO
    """,

    "exits": {"west": "Woods"},

    "items": []
}

location_beach = {
    "name": "Beach",

    "description":
    """
    TODO
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
