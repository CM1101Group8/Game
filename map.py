from items import *
from enemies import *
#starting location
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

    "visited": True,

    "enemy": ""
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

    "items": [item_wood],

    "visited": True,

    "enemy": ""
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

    "items": [item_wood],

    "visited": True,

    "enemy": ""
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

    "items": [item_wood],

    "visited": True,

    "enemy": ""
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

    "visited": True,

    "enemy": ""
}

location_ravine = {
    "name": "Ravine",

    "description":
    """
    You have found the Ravine, easily the most colourful 
    and arguably the most beautiful part of the island. 
    The smooth aquamarine water softly kisses the area 
    that surrounds it. There is an abundance of plant 
    life here. It is possible that could be useful.
    """,

    "exits": {"south": "MON2", "west": "Brush", "east": "MON1", "north": "River"},

    "items": [item_leaves],

    "visited": True,

    "enemy": ""
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

    "visited": True,

    "enemy": ""
}

location_rockside = {
    "name": "Rockside",

    "description":
    """
    You arrive at the rocky shore of the island; it is 
    blisteringly cold and the sea crashes up against and 
    batters the stone walls; it is unsafe here. You do however 
    notice something, or more someone, peculiar. You approach the 
    figure and recognise the corpse of ex-SAS and survivalist 
    expert Bear Grylls, stripped down to absolutely nothing but 
    the skin of a seal carcass. At least you out-survived him.
    There appears to be some sort of tool on his body.
    """,

    "exits": {"east": "MON2"},

    "items": [item_sparktool],

    "visited": True,

    "enemy": ""
}

location_woods = {
    "name": "Dry Woods",

    "description":
    """
    You find yourself in an extremely dense part of the map. 
    You look above and see the abundance of trees that fight 
    over sunlight, as a result hardly any sunlight actually has 
    a chance to make it to the ground, so the area isn't well 
    lit and the plant life on ground level barely survives, they 
    do not have their natural colour. A lot of dead plant life 
    reside here. Fortunately, it is dry here and it is possible 
    to obtain good wood for a fire.
    """,

    "exits": {"west": "MON1", "east": "Cliffs", "south": "MON3", "north": "Hill"},

    "items": [item_wood, item_fireblanket],

    "visited": True,

    "enemy": ""
}

location_cliffs = {
    "name": "Cliffs",

    "description":
    """
    You find yourself at the edge of a cliff. The sun graces 
    the sea and lights up your face and the surrounding area. 
    However, it isn't entirely idyllic here. At the cliffs, 
    is a man, a crazed man, with his clothes torn up, his face 
    and hair covered in mud and blood, and with razor cuts 
    covering his face and arms. You realise it's an engraged 
    Kirill ready to attack!
    """,

    "exits": {"west": "Woods"},

    "items": [item_rope],

    "visited": True,

    "enemy": enemy_kirill
}

location_beach = {
    "name": "Beach",

    "description":
    """
    You find yourself at the expansive beach of the island. 
    Although it is a beautiful vista to behold, especially when 
    the sun sets, you can't help but distrust its beauty as after 
    all, you are stranded on an island with a very high possibility 
    of remaining here and dying. There's a medi-kit and a bag of
    crisps. It's your lucky day... ish.
    """, 

    "exits": {"west": "MON3"},

    "items": [item_medkit, item_crisps],

    "visited": True,

    "enemy": ""
}

location_passage = {
    "name": "Dark Passage",

    "description":
    """
    You reach a very dark and ominous passage that is haunted 
    by cold and daunting whispers. You are greeted by a pack of 
    fiendish ghost creatures, ghouls, who prey on the dark and the 
    weak. They have every intent to take your soul and kill you.
    """,

    "exits": {"south": "HOF", "north": "Lair", "west": "Cave"},

    "items": [],

    "visited": True,

    "enemy": ""
}

location_river = {
    "name": "River",

    "description":
    """
    You arrive at the main river that flows through the island. 
    It's a source of life for all the wildlife here. You 
    notice a brightly coloured cloth sat atop a hill of sorts 
    to the West, although you can't quite figure out what.
    """,

    "exits": {"west": "Waterfall", "east": "HOF", "south": "Ravine"},

    "items": [],

    "visited": True,

    "enemy": ""
}

location_waterfall = {
    "name": "Waterfall",

    "description":
    """
    At the end of the river lies a waterfall, and clinging
    onto a tree on top of that waterfall is a fluorescent 
    parachute. It is impossible to climb simply by yourself. 
    You notice that there is a very clear overhead between 
    the waterfall and the ravine, if only you had the means 
    the traverse this open path….
    """,

    "exits": {"east": "River"},

    "items": [item_parachute],

    "visited": True,

    "enemy": ""
}

location_hill = {
    "name": "Hill",

    "description":
    """
    You arrive at a forest hillside, the hill is quite steep 
    but scalable, what isn't easily scalable is the stone wall 
    atop of the hill. At the top of the wall you notice a small 
    opening, big enough for you to squeeze into, however you 
    aren't Spiderman so you won't be climbing that in a hurry.
    """,

    "exits": {"west": "HOF", "south": "Woods"},

    "items": [item_wood],

    "visited": True,

    "enemy": ""
}

def on_enter_cave(player, locations, nice_print, Fore, Back, take_damage):
    take_damage(player, 70)
    return True

location_cave = {
    "name": "Fire cave",

    "description": 
    """
    You approach a sinister-looking cave with an entrance that 
    is engulfed in flames. You see one of the plane's engines is 
    lodged into the wall of the cave. You can enter the cave if 
    you wish but it will hurt; A LOT.
    """,

    "exits": {"east": "Passage"},

    "items": [item_gun],

    "visited": True,

    "enemy": "",

    "on_enter": on_enter_cave
}

location_cave2 = {
    "name": "Flooded cave",

    "description": 
    """
    You enter the cave; the water reaches close to the height 
    of your knees, the water is very cold. In the water you 
    see a case floating about and are intrigued.
    """,

    "exits": {"west": "Passage", "south": "Hill"},

    "items": [item_bullets],

    "visited": True,

    "enemy": ""
}

location_lair = {
    "name": "Wolf's lair",

    "description": 
    """
    You already know this is a bad place to be. The 
    entrance to this place is covered in the carcasses 
    of other animals and dried blood paints the walls. There 
    is a foul stench that worsens the further you walk in this 
    cave. You hear a vicious growl that vibrates the walls 
    and floors, rendering you still where you stand. Suddenly, 
    a brooding Werewolf emerges from the shadows and hits you 
    from the side, making you crash into the ground with a 
    thump. You lose 30 health.
    """,

    "exits": {"south": "Passage"},

    "items": [item_petrol],

    "visited": True,

    "enemy": enemy_wolf
}
#dictionary of locations
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
    "Lair": location_lair



}
