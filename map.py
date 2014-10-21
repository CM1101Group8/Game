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

    "exits": {"west": "MON2", "north": "MON1", "east": "MON3"},

    "items": [],

    "visited": False
}

location_mon1 = {
    "name": "Middle of Nowhere",

    "description":
    """
    You reach 'The Middle of Nowhere', and this is exactly
    where you are situated. There is nothing of interest in
    the immediate vicinity, besides wood and trees. At this point,
    the only useful thing to do is to choose another direction to go in.
    """,

    "exits": {"east": "Woods", "north": "HOF", "west": "Ravine", "south": "Plane"},

    "items": [],

    "visited": False
}

location_mon2 = {
    "name": "Middle of Nowhere",

    "description":
    """
    You reach 'The Middle of Nowhere', and this is exactly
    where you are situated. There is nothing of interest in
    the immediate vicinity, besides wood and trees. At this point,
    the only useful thing to do is to choose another direction to go in.
    """,

    "exits": {"north": "Ravine", "west": "Rockside", "east": "Plane"},

    "items": [],

    "visited": False
}

location_mon3 = {
    "name": "Middle of Nowhere",

    "description":
    """
    You reach 'The Middle of Nowhere', and this is exactly
    where you are situated. You find the charred corpses of Owen
    and Beru Lars. They have nothing to help you survive, it is
    best to move on.
    """,

    "exits": {"west": "Plane", "east": "Beach", "north": "Woods"},

    "items": [],

    "visited": False
}

location_hof = {
    "name": "Heart of the Forest",

    "description":
    """
    You are now in the heart of the forest. Without
    your head torch, you cannot see anything. It is
    no use trying to look at your compass. Surrounded
    by the darkness, you begin to feel lightheaded,
    and anxiously turn your head and try to sharpen
    your hearing; you fear something is approaching.
    """,

    "exits": {"south": "MON1", "north": "Passage", "west": "River", "east": "Hill"},

    "items": [item_wood],

    "visited": False
}

location_ravine = {
    "name": "Ravine",

    "description":
    """
    You are now at the ravine. It is peaceful here,
    and there is a pile of leaves on the ground.
    It is possible those may be useful.
    """,

    "exits": {"south": "MON2", "west": "Brush", "east": "MON1", "north": "River"},

    "items": [item_leaves],

    "visited": False
}

location_brush = {
    "name": "Barbed Brush",

    "description":
    """
    You have stumbled into the barbed brush, an area covered
    in horrible looking plants, both sharp and dry in appearance,
    it appears dead. The breathing here isn't entirely pleasant,
    the atmosphere is humid and the air is salty. Although it
    would appear to be a very salty area, the brush here could
    be easily set alight.
    """,

    "description_alight":
    """
    Whatever life remained in the plants here quickly
    escape and the flames uncover a body of an unusual man;
    a scarred face, a long, thin moustache, and a muscular
    body with large tattoos holding a well-intact machete.
    It is unknown how long this body has been here for.
    """,

    "exits": {"east": "Ravine"},

    "items": [item_wood],

    "visited": False
}

location_rockside = {
    "name": "Rockside",

    "description":
    """
    You are now at the rockside. Amongst all
    the rocks there is a scary but satisfying sight:
    Bear Grylls' corpse. At least you out-survived him.
    There appears to be some sort of tool on his body.
    """,

    "exits": {"east": "MON2"},

    "items": [item_sparktool],

    "visited": False
}

location_woods = {
    "name": "Dry Woods",

    "description":
    """
    You are in the woods. It is dingy and
    very dry, much like the pile of wood on the floor.

    """,

    "exits": {"west": "MON1", "east": "Cliffs", "south": "MON3", "north": "Hill"},

    "items": [item_wood],

    "visited": False
}

location_cliffs = {
    "name": "Cliffs",

    "description":
    """
    You're at the cliffs. It's high up, and there is
    some climbing rope. You have a great view of...
    CRAZY ANGRY KIRILL TRYING TO KILL YOU FOR YOUR POOR TEST SCORE.
    """,

    "exits": {"west": "Woods"},

    "items": [item_rope],

    "visited": False
}

location_beach = {
    "name": "Beach",

    "description":
    """
    You're on a nice island beach. It's pleasant...
    until you remember you're stranded on an island
    trying not to die. There's a medi-kit and a bag of
    crisps. It's your lucky day... ish.
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

    "exits": {"south": "HOF", "north": "Lair", "west": "Cave"},

    "items": [],

    "visited": False
}

location_river = {
    "name": "River",

    "description":
    """
    TODO
    """,

    "exits": {"west": "Waterfall", "east": "HOF", "south": "Ravine"},

    "items": [],

    "visited": False

}

location_waterfall = {
    "name": "Waterfall",

    "description":
    """
    TODO
    """,

    "exits": {"east": "River"},

    "items": [],

    "visited": False
}

location_hill = {
    "name": "Hill",

    "description":
    """
    TODO

    It looks like there is a cave above you. If only you
    had a way of getting there...
    """,

    "exits": {"west": "HOF", "south": "Woods"},

    "items": [],

    "visited": False
}

location_cave = {
    "name": "Fire cave",

    "description":
    """
    TODO
    """,

    "exits": {"east": "Passage"},

    "items": [],

    "visited": False
}

location_cave2 = {
    "name": "Flooded cave",

    "description":
    """
    TODO
    """,

    "exits": {"west": "Passage", "south": "Hill"},

    "items": [],

    "visited": False
}

location_lair = {
    "name": "Wolf's lair",

    "description":
    """
    TODO
    """,

    "exits": {"south": "Passage"},

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
    "Passage": location_passage,
    "River": location_river,
    "Waterfall": location_waterfall,
    "Hill": location_hill,
    "Cave": location_cave,
    "Cave2": location_cave2,
    "Lair": location_cave



}
