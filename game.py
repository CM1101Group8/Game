#!/usr/bin/python3

import sys, time
from colorama import init, Fore, Back

from map import locations
from player import *
from items import *
from gameparser import *
from combat import *
from helpers import *

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

    """
    nice_print_line("You can:")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))
    for things in inv_items:
        if "heal" in things.keys():
            nice_print_line("USE " + things["id"].upper() + " to heal using your " + things["name"] + ".")
        elif "use" in things.keys():
            nice_print_line("USE " + things["id"].upper() + " to use your " + things["name"] + ".")
        if "use_with" in things.keys():
            for item in inv_items:
                if things["use_with"] == item["id"]:
                    nice_print_line("USE " + things["id"].upper() + " WITH "+ things["use_with"].upper() +" to create " + things["combined_item"]["name"] + ".")
    for things in location_items:
        nice_print_line("TAKE " + things["id"].upper() + " to take a " + things["name"] + ".")
    for things in inv_items:
        nice_print_line("DROP " + things["id"].upper() + " to drop your " + things["name"] + ".")

    nice_print("What do you want to do?")

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
            if player["inventory_weight"] + item["mass"] < 4000:    #Checks if player inventory is light enough to carry item
                player["current_location"]["items"].remove(item)
                player["inventory"].append(item)
                player["inventory_weight"] += item["mass"]
                nice_print("You picked up a " + item["name"] + ".", Fore.GREEN)
                nice_print(item["description"])
                print()
                return True
            else:
                nice_print("\nYou do not have room for an item that heavy.", Fore.RED)
                return False
    if not item_taken:
        nice_print("You cannot take that.", Fore.RED)
        return False

def execute_drop(item_ident):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current location. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    item_dropped = 0
    for item in player["inventory"]:
        if item_ident == item["id"]:        #if player drops item it is removed from inventory and the mass subtracted
            item_dropped = 1
            player["inventory"].remove(item)
            player["current_location"]["items"].append(item)
            player["inventory_weight"] -= item["mass"]
            nice_print("You dropped your " + item["name"] + ".", Fore.GREEN)
            return True
    if not item_dropped:
        nice_print("You cannot drop that.", Fore.RED)
        return False


def execute_use(item_id):
    """Allows player to use items they have in their inventory. If not in inventory 
        then it will print "You don't have that"
    """

    for item in player["inventory"]:
        if item_id == item["id"]:
            #The item uses are functions referenced inside the item list, the item is checked for a function and if one is found it is executed
            if "heal" in item.keys():
                heal_player(player, item["name"], item["heal"])
                player["inventory"].remove(item)
                player["inventory_weight"]  -= item["mass"]
                return True
            elif "use" in item.keys():
                item["use"](player, locations, nice_print, Fore, Back)
                return True
            else:
                nice_print("You cannot use this.", Fore.RED)
                nice_print(item["description"])
                print()
                return False
    nice_print("You don't have that!", Fore.RED)
    return False

def execute_use_with(item_one_id, item_two_id):
    """This function deals with the combination of items. It first checks
    if the player has the items in their inventory and if the items
    can be combined. Some items can only be combined in a certain
    location.
    """
    # Check if the first item is in the player's inventory
    for item_one in player["inventory"]:
        if item_one_id == item_one["id"]:
            # Check if this item has another item it can be used with
            if "use_with" in item_one.keys():
                # Check if the second item is in the player's inventory
                for item_two in player["inventory"]:
                    if item_two_id == item_two["id"]:
                        # Check if these items can be combined
                        if item_one["use_with"] == item_two["id"]:
                            # Check if we are in the correct location to combine this items, if applicable
                            if "combine_location" in item_one.keys() and player["current_location"]["name"] != item_one["combine_location"]:
                                nice_print("You can't combine those items here. Try somewhere else. " + item_one["combine_location"] + " maybe...", Fore.RED)
                                return False

                            # Check the player's inventory won't be too heavy after combining these items
                            if player["inventory_weight"] - item_one["mass"] - item_two["mass"] + item_one["combined_item"]["mass"] < 4000:
                                # Remove the weight of the original items and add the weight of the new item
                                player["inventory"].remove(item_one)
                                player["inventory_weight"] -= item_one["mass"]
                                player["inventory"].remove(item_two)
                                player["inventory_weight"] -= item_two["mass"]
                                player["inventory"].append(item_one["combined_item"])
                                player["inventory_weight"] += item_one["combined_item"]["mass"]
                                nice_print("You combined "+ item_one["name"] + " with "+ item_two["name"] +" and made "+ item_one["combined_item"]["name"] + ".", Fore.GREEN)
                                return True
                                
                            else:
                                nice_print("You could combine these items, but it would be too heavy for you to carry.", Fore.RED)
                                return False                                
                        else:
                            nice_print("Those items don't go together. Try another combination.", Fore.RED)
                            return False
            else:
                nice_print("Those items don't go together. Try another combination.", Fore.RED)
                return False

    nice_print("You don't have that item.", Fore.RED)
    return False                    

def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", "drop" or "use"), executes either execute_go,
    execute_take, execute_drop, execute_use or execute_use_with, supplying 
    the other command as the argument.
    """
    if len(command) > 1:
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
                    return execute_use_with(command[1], command[3])
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
    with the name given by "direction".
    """

    # Next location to go to
    return locations[exits[direction]]

def title():
    """This function prints title in large font with blue background,
    as well as the introduction text. Uses colorama library to add 
    colour to the title.
    """

    print()
    nice_print_line(
            """
        _______________________________________________________________        
       |    _____ _______ _____            _   _ _____  ______ _____   |       
       |   / ____|__   __|  __ \     /\   | \ | |  __ \|  ____|  __ \  |       
       |  | (___    | |  | |__) |   /  \  |  \| | |  | | |__  | |  | | |       
       |   \___ \   | |  |  _  /   / /\ \ | . ` | |  | |  __| | |  | | |       
       |   ____) |  | |  | | \ \  / ____ \| |\  | |__| | |____| |__| | |       
       |  |_____/   |_|  |_|  \_\/_/    \_\_| \_|_____/|______|_____/  |       
       |_______________________________________________________________|       
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

def title_input():
    """This function displays the menu and accepts input at the beginning
    of the game. Allows user to start playing or view credits.
    """
    nice_print_line("Type START to start the game")
    nice_print_line("Type CREDITS for the credits")

    command = input("> ").upper()
    while command != "START" and command != "CREDITS":
        command = input("> ").upper()

    if command == "START":      #if user enters start, goes to main game function
        return
    elif command == "CREDITS":
        credits()

def credits(end=False):
    """This function prints the credits so you know we made the game. Has an end
    parameter to specify whether the credits are being displayed after the game
    has been completed.
    """

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
    if not end:
        title_input()

# This is the entry point of our program
def main():
    # Initialise colorama
    init()
    # Show title screen
    title()
    # Main game loop
    while True:
        # Check if the player's health is below zero and end the game
        if player["health"] <= 0:
            nice_print("You have died! Game over!", Fore.RED)
            quit()

        # Check if the player has met the victory condition and end the game    
        if item_fire in player["inventory"]:
            nice_print_line("Your fire now burns brightly on the top of the cliffs")
            nice_print_line("Any passing planes or ships are sure to see you on the island")
            nice_print_line("But will anyone arrive in time, or is it already too late for you?")
            nice_print_line("Only time will decide")
            credits(1)
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

        # Execute the player's command - repeat the options if the command cannot be performed
        while not execute_command(command):
            command = menu(player["current_location"]["exits"], player["current_location"]["items"], player["inventory"])



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
