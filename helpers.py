from game import *

def item_damage(item):
    """This function calculates the amount of damage a certain item will
    deal based on the square root of the item's mass.
    """
    import math
    return int(math.sqrt(item['mass']))

def take_damage(player, damage):
    """This function inflicts a specified amount of damage on the player.
    """

    player['health'] = player['health'] - int(damage)
    nice_print_line("You took "+ str(damage) +" damage.", Fore.RED)
    nice_print_line("Your health is now "+ str(player['health']) +".")
    return player

def heal_player(player, item, heal_amount):
    """This function heals the player for a certain amount of health.
    """

    player["health"] = player["health"] + int(heal_amount)
    #Health cannot go over a pre-defined max
    if player["health"] > 100:
        player["health"] = 100
    nice_print_line("You use the "+ str(item) +" and gain "+ str(heal_amount) +" health.", Fore.GREEN)
    nice_print_line("Your health is now "+ str(player['health']) +".")
    return player

def print_player(player):
    """This function prints the player's current status.
    """
    nice_print_line("Your health is: " + str(player["health"]), Fore.RED)
    print()

def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string).
    """

    list = []
    for x in items:
     list.append(x["name"])

    return ', '.join(list)


def print_location_items(location):
    """This function takes a location as an input and nicely displays a list of items
    found in this location (followed by a blank line). If there are no items in
    the location, nothing is printed. See map.py for the definition of a location, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names.
    """

    items = list_of_items(location["items"])
    if items:
        nice_print_line("There is "+ items + " here.")
        print()


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_location_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.".
    """

    items = list_of_items(items)
    if items:
      nice_print_line("You have "+ items + ".")
      print()


def print_location(location):
    """This function takes a location as an input and nicely displays its name
    and description. The location argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the location
    is printed in all capitals and framed by blank lines. Then follows the
    description of the location and a blank line again. If there are any items
    in the location, the list of items is printed next followed by a blank line
    (use print_location_items() for this).
    """

    if "on_print" in location.keys():
        location["on_print"](player, locations, nice_print, Fore, Back, take_damage)
    print()
    nice_print(location["name"].upper(), Fore.BLACK, Back.WHITE)
    print()
    #If the area is visited for the first time, the whole description is nice printed, and the visited variable is changed
    if not location["visited"]:
        nice_print(location["description"])
        location["visited"] = True
    #Otherwise the whole description is printed at once to save the players time
    else:
        nice_print_line(location["description"])
    print()

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the location into which
    this exit leads.
    """
    return locations[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the location into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.
    """
    nice_print_line("GO " + direction.upper() + " to the " + leads_to + ".")

def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    """
    return chosen_exit in exits

def nice_print(text, fore=Fore.WHITE, back=Back.BLACK):
    """This function stops text appearing in one block and instead makes it
    appear letter by letter. This also supports adding colour to text using
    the Colorama library.
    """

    print(fore + back, end='')
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    print(Fore.RESET + Back.RESET, end='\n')

def nice_print_line(text, fore=Fore.WHITE, back=Back.BLACK):
    """This function delays the printing of lines to make the lines of text
    appear one by one. This also supports adding colour to text using
    the Colorama library.
    """

    print(fore + back, end='')
    print(text, end='')
    time.sleep(0.2)
    print(Fore.RESET + Back.RESET, end='\n')
