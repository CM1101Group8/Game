#!/usr/bin/python3

import sys, time
from colorama import init, Fore, Back

from map import locations
from player import *
from items import *
from gameparser import *

def combat(enemy):
    correct_item = 0
    nice_print("WARNING")
    warning = "There is a " + enemy["name"] + " in the area with you."
    nice_print(warning)
    while True:
        if player["health"] < 1:
            print("Player has died, RIP in peace")
            quit()
        #Checks too see if the player has the correct item to defeat the enemy
        nice_print_line("Your health is: " + str(player["health"]), Fore.RED)
        for item in player["inventory"]:
            print("USE", item["id"].upper(), "to attack", enemy["name"], "with", item["name"] + ".")
            if item["id"] == enemy["vuln"]:
                correct_item = 1
        if correct_item:
            nice_print("You have the correct equipment to defeat")
        if not correct_item:
            nice_print("You do not have the correct item to deal with the enemy")
            nice_print("You can attempt to attack him with other items or FLEE")
        print ("FLEE to return to the previous area.")
        #Gets the players command and normalises it
        command = normalise_input(input(">"))
        if command:
            #checks what the player wants to do
            if command[0] == "use":
                if len(command) > 1:
                    for item in player["inventory"]:
                        if item["id"] == command[1]:
                            item_used = item
                    if command[1] == enemy["vuln"]:
                        success = "You succesfully hit " + enemy["name"] + " with " + item_used["name"] + ", killing them."
                        nice_print(success)
                        player["current_location"]["enemy"] = ""
                        break

                    else:
                        print("You attempt to attack", enemy["name"], "with", command[1])
                        print(enemy["name"], "is impervious to your", command[1], "based attack")
                        print("The attack backfires and deals", item_damage(item_used), "damage to yourself.")
                        player["health"] -= item_damage(item_used)

            elif command[0] == "flee":
                player["current_location"] = player["previous_location"]
                break

            else:
                nice_print("You cannot do that now")
        else:
            nice_print("You cannot do nothing")

def item_damage(item):
    #calculates item damage
    import math
    return int(math.sqrt(item['mass']))

def take_damage(player, damage):
    #inflicts damage on the player
    player['health'] = player['health'] - int(damage)
    nice_print_line(""+ player['name'] +" took "+ str(damage) +" damage.")
    nice_print_line(""+ player['name'] +" health is now "+ str(player['health']) +".")
    return player

def print_player(player):
    #prints the player status
    nice_print_line("Your health is: " + str(player["health"]), Fore.RED)
    nice_print_line("Your experience is: "+str(player["experience"]), Fore.YELLOW)
    print()

def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'

    >>> list_of_items([item_id])
    'id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'

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
    to produce a comma-separated list of item names. For example:

    >>> print_location_items(locations["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_location_items(locations["Office"])
    There is a pen here.
    <BLANKLINE>

    >>> print_location_items(locations["Robs"])

    (no output)

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """
    items = list_of_items(location["items"])
    if items:
        nice_print_line("There is "+ items + " here.")
        print()


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_location_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have id card, laptop, money.
    <BLANKLINE>

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
    (use print_location_items() for this). For example:

    >>> print_location(locations["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    >>> print_location(locations["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_location(locations["Robs"])
    <BLANKLINE>
    ROBS' ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    location. Inside you notice Rob Evans and Rob Davies. They
    ignore you. To the north is the reception.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    print()
    nice_print(location["name"].upper(), Fore.BLACK, Back.WHITE)
    print()
    if not location["visited"]:
        nice_print(location["description"])
        location["visited"] = True
    else:
        nice_print_line(location["description"])
    print()

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the location into which
    this exit leads. For example:

    >>> exit_leads_to(locations["Reception"]["exits"], "south")
    "Robs' room"
    >>> exit_leads_to(locations["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(locations["Tutor"]["exits"], "west")
    'Reception'
    """
    return locations[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the location into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "Robs' room")
    GO SOUTH to Robs' room.
    """
    nice_print_line("GO " + direction.upper() + " to the " + leads_to + ".")


def print_menu(exits, location_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments location_items and inv_items are the items lying around in the location
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The location into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the location print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to Robs' room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    nice_print_line("You can:")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))
    for things in inv_items:
        if "use" in things.keys():
            nice_print_line("USE " + things["id"].upper() + " to use your " + things["name"] + ".")
    for things in location_items:
        nice_print_line("TAKE " + things["id"].upper() + " to take " + things["name"] + ".")
    for things in inv_items:
        nice_print_line("DROP " + things["id"].upper() + " to drop " + things["name"] + ".")

    nice_print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(locations["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(locations["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(locations["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(locations["Parking"]["exits"], "east")
    True
    """
    return chosen_exit in exits


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current location
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the location into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global player
    if is_valid_exit(player["current_location"]['exits'], direction):
        player["previous_location"] = player["current_location"]
        player["current_location"] = move(player["current_location"]['exits'], direction)
        if "on_enter" in player["current_location"].keys():
            return player["current_location"]["on_enter"](player, locations, nice_print, Fore, Back, take_damage)
        return True
    else:
        nice_print("You cannot go there!", Fore.RED)
        return False


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current location to the player's inventory. However, if
    there is no such item in the location, this function prints
    "You cannot take that."
    """
    item_taken = 0
    for item in player["current_location"]["items"]:
        if item_id == item["id"]:
            item_taken = 1
            if player["inventory_weight"] + item["mass"] < 3000:    #Checks if player inventory is light enough to carry item     
                player["current_location"]["items"].remove(item)
                player["inventory"].append(item)
                player["inventory_weight"] += item["mass"]
                nice_print("You picked up " + item["name"] + ".", Fore.GREEN)
                nice_print(item["description"])
                print()
                return True
            else:
                nice_print("\nYou do not have room for an item that heavy", Fore.RED)
                return False
    if not item_taken:
        nice_print("You cannot take that", Fore.RED)
        return False

def execute_drop(item_ident):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current location. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    item_dropped = 0
    for item in player["inventory"]:
        if item_ident == item["id"]:
            item_dropped = 1
            player["inventory"].remove(item)
            player["current_location"]["items"].append(item)
            player["inventory_weight"] -= item["mass"]
            nice_print("You dropped " + item["name"] + ".", Fore.GREEN)
            return True
    if not item_dropped:
        nice_print("You cannot drop that", Fore.RED)
        return False


def execute_use(item_id):
#Allows player to use items they have in their inventory. If not in invewntory then it will print "You don't hav that"     

    for item in player["inventory"]:
        if item_id == item["id"]:
            if "use" in item.keys():
                item["use"](player, locations, nice_print, Fore, Back)
                return True
            else:
                nice_print("You cannot use this.", Fore.RED)
                nice_print(item["description"])
                print()
                return False
    nice_print("You don't have that!", Fore.RED)
    return False

def execute_use_with(item_one, item_two):
    #global locations
    #if player["current_location"] == locations["Cliffs"]:
        #for item in player["inventory"]: 
        #nice_print_line("You combined "+ item_one + " with "+ item_two +" and made "+ created_item + ".")
    pass
    
def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """
    if command[0] == "go":
        if len(command) > 1:
            return execute_go(command[1])
        else:
            nice_print("Go where?", Fore.YELLOW)
            return False

    elif command[0] == "take":
        if len(command) > 1:
            return execute_take(command[1])
        else:
            nice_print("Take what?", Fore.YELLOW)
            return False

    elif command[0] == "drop":
        if len(command) > 1:
            return execute_drop(command[1])
        else:
            nice_print("Drop what?", Fore.YELLOW)
            return False

    elif command[0] == "use":
        if len(command) > 1:
            if len(command) > 2 and command[2] == "with" and len(command[3]) > 0:
                execute_use_with(command[1], command[3])
            else:
                return execute_use(command[1])
        else:
            nice_print("Use what?", Fore.YELLOW)
            return False

    else:
        nice_print("This makes no sense.", Fore.YELLOW)
        return False


def menu(exits, location_items, inv_items):
    """This function, given a dictionary of possible exits from a location, and a list
    of items found in the location and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, location_items, inv_items)

    # Read player's input
    user_input = input("> ")
    while user_input == "":
        user_input = input("> ")
    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the location into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(locations["Reception"]["exits"], "south") == locations["Robs"]
    True
    >>> move(locations["Reception"]["exits"], "east") == locations["Tutor"]
    True
    >>> move(locations["Reception"]["exits"], "west") == locations["Office"]
    False    """

    # Next location to go to
    return locations[exits[direction]]

def nice_print(text, fore=Fore.WHITE, back=Back.BLACK):
    # Function stops text appearing in one block and instead makes it appear word by word
    print(fore + back, end='')
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.035)
    print(Fore.RESET + Back.RESET, end='\n')

def nice_print_line(text, fore=Fore.WHITE, back=Back.BLACK):
    print(fore + back, end='')
    print(text, end='')
    time.sleep(0.35)
    print(Fore.RESET + Back.RESET, end='\n')

def title():    #prints title in large font with blue background. Uses colorama library.
    print()
    nice_print_line(
        """

           _____ _______ _____            _   _ _____  ______ _____  
          / ____|__   __|  __ \     /\   | \ | |  __ \|  ____|  __ \ 
         | (___    | |  | |__) |   /  \  |  \| | |  | | |__  | |  | |
          \___ \   | |  |  _  /   / /\ \ | . ` | |  | |  __| | |  | |
          ____) |  | |  | | \ \  / ____ \| |\  | |__| | |____| |__| |
         |_____/   |_|  |_|  \_\/_/    \_\_| \_|_____/|______|_____/                                                   
        """, Fore.WHITE, Back.CYAN)
    print()
    nice_print(
    """
    You are an unwary passenger of a plane that is in freefall,
    after what you now understand is because of an engine failure.
    As you look outside of the window, you see the plane has found
    itself in the middle of a horrific storm, the crew and passengers
    are in an insane panic state; they viciously fight over the few
    available parachutes. One of the passengers has managed to open
    one of the exit doors, which does not result in fruitful salvation.
    The passenger as well as others are sucked out of the plane in a
    moment's notice, it's a devastating sight to witness. You accept
    your fate, there is no hope, and your senses aren't as they should
    be; your vision is blurred. You take your seat and close your eyes...
    """)
    print()
    title_input()

def title_input():      #starting menu at beginning of game. Allows user to start playing or view credits
    nice_print_line("Type START to start the game")
    nice_print_line("Type CREDITS for the credits")

    command = input("> ").upper()
    while command != "START" and command != "CREDITS":
        command = input("> ").upper()

    if command == "START":
        return
    elif command == "CREDITS":
        credits()

def credits():      #prints credits so you know we made the game
    print()
    nice_print("CREDITS", Fore.BLACK, Back.WHITE)
    print()
    nice_print("   Stranded was developed by:", Fore.YELLOW)
    nice_print_line("       Thomas Durston")
    nice_print_line("       Isobel Speed")
    nice_print_line("       Caitlin Taylor")
    nice_print_line("       Edward Trist")
    nice_print_line("       Samuil Velichkov")
    nice_print_line("       Michael Whitfield")
    nice_print_line("       Jamie Williamson")
    print()
    nice_print("   With thanks to:", Fore.YELLOW)
    nice_print_line("       Colorama - https://pypi.python.org/pypi/colorama")
    nice_print_line("       ASCII Text Art from - http://patorjk.com/software/taag")
    print()
    nice_print("   Thanks for playing!", Fore.GREEN)
    print()
    title_input()

# This is the entry point of our program
def main():
    # Initialise colorama
    init()
    # Show title screen
    title()
    # Main game loop
    while True:
        if player["health"] <= 0:
            nice_print("You have died! Game over!", Fore.RED)
            quit()
        # Display game status (location description, inventory etc.)
        print_location(player["current_location"])
        if player["current_location"]["enemy"]:
            combat(player["current_location"]["enemy"])
            print_location(player["current_location"])
        print_player(player)
        print_inventory_items(player["inventory"])

        # Show the menu with possible actions and ask the player
        command = menu(player["current_location"]["exits"], player["current_location"]["items"], player["inventory"])

        # Execute the player's command
        while not execute_command(command):
            command = menu(player["current_location"]["exits"], player["current_location"]["items"], player["inventory"])



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
