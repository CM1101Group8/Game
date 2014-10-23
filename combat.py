from game import *

def combat(enemy):
    """This function deals with the combat system in the game, including input
    and logic.
    """

    correct_item = 0
    #Informs the player of the enemies presense then holds them in the combat menuwith a while loop
    nice_print("WARNING", Fore.BLACK, Back.WHITE)
    nice_print("There is a " + enemy["name"] + " in the area with you.")
    while True:
        #Checks if the player died during the previous round of combat, and if so quits the game
        if player["health"] < 1:
            print("Player has died, RIP in peace")
            quit()

        nice_print_line("\nYour health is: " + str(player["health"]), Fore.RED)
        #Prints the list of USE options the player has based on his inventory
        for item in player["inventory"]:
            print("USE", item["id"].upper(), "to attack", enemy["name"], "with", item["name"] + ".")
            if item["id"] == enemy["vuln"]:
                correct_item = 1
                nice_print("You have the correct equipment to defeat")
        #Only prints these lines if the correct item to defeat the enemy is not in the palyer's inventory
        if not correct_item:
            nice_print("You do not have the correct item to deal with the enemy")
            nice_print("You can attempt to attack him with other items or FLEE")
        print ("FLEE to return to the previous area.")
        #Gets the players command and normalises it
        command = normalise_input(input("> "))
        if command:
            #checks what the player wants to do
            if command[0] == "use":
                item_used = ""
                if len(command) > 1:
                    #puts the used items list in to a variable for later reference
                    for item in player["inventory"]:
                        if item["id"] == command[1]:
                            item_used = item
                    #If the item chosen is the one the enemy is vulnerable too, the enemy is removed from the room and the While loop broken out of
                    if command[1] == enemy["vuln"] and item_used:
                        success = "You successfully hit " + enemy["name"] + " with " + item_used["name"] + ", killing them."
                        nice_print(success, Fore.GREEN)
                        player["current_location"]["enemy"] = ""
                        if "on_kill" in enemy.keys():
                            enemy["on_kill"](player, locations)
                        break
                    #If the wrong item is used, it backfires on the player for some damage based on the weight of the item
                    else:
                        #This checks if the item actually exists, it is unessacery to check this earlier because if an enemy
                        #is vulnerable to the item then the item must exist
                        if item_used:
                            nice_print("You attempt to attack " + enemy["name"] + " with " + command[1])
                            nice_print(enemy["name"] + " is impervious to your " + command[1] + " based attack")
                            nice_print("The attack backfires and deals " + str(item_damage(item_used)) + " damage to yourself.", Fore.RED)
                            player["health"] -= item_damage(item_used)
                        else:
                            nice_print("Use what?", Fore.YELLOW)
            #FLEE only allows the player to return to their previous location so they do not get to locations they are not allowed to acess yet
            #This is done by storing the previous location into a player variable every time the player moves
            elif command[0] == "flee":
                player["current_location"] = player["previous_location"]
                break

            else:
                nice_print("You cannot do that now")
        else:
            nice_print("You cannot do nothing")