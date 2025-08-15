
import os
from data import *

# clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# show players location
def show_location(locations, location_name):
    if location_name not in locations:
        print(f"\nERROR: Location '{location_name}' is an invalid option.")
        return
    
    current_location = locations.get(location_name)
    
    print("\nYou are in", location_name.upper())
    print()
    
    items = current_location.get("items", [])
    if items:
        print("You see:", ", ".join(items))
    
    exits = current_location.get("exits", {})
    if exits:
        print("Exits:", ", ".join(exits.keys()))
    else:
        print("There are no obvious paths.")


# directions
def get_command():
    return input("\nWhat direction do you go? ").strip().lower()


# movement
def move(current_location, direction, locations):
    if direction in locations[current_location]["exits"]:
        return locations[current_location]["exits"][direction]
    else:
        print("The path does not go that way. It would be dangerous to continue.")
        return current_location

def move1(direction):
    if player["location"] == "Start":
        if direction == "go right":
            player["location"] = "Halivaara"
        elif direction == "go straight":
            player["location"] = "Vergamo"
        elif direction == "go left":
            player["location"] = "Falkirk"
    elif player["location"] == "Halivaara":
        if direction == "go right":
            player["location"] = "Naporia"
        elif direction == "go left":
            player["location"] = "Vergamo"
    elif player["location"] == "Vergamo":
        if direction == "go right":
            player["location"] = "Cross Roads"
        elif direction == "go left":
            player["location"] = "Cross Roads"
    elif player["location"] == "Cross Roads":
        if direction == "go north":
            player["location"] = "Peltragow"
        elif direction == "go south":
            player["location"] = "Blencargo"
    elif player["location"] == "Falkirk":
        if direction == "go right":
            player["location"] = "Luneburg"
    elif player["location"] == "Peltragow":
        if direction == "go back":
            player["location"] = "Cross Roads"
    elif player["location"] == "Blencargo":
        if direction == "go back":
            player["location"] = "Cross Roads"
    elif player["location"] == "Luneburg":
        if direction == "go back":
            player["location"] = "Falkirk"
    elif player["location"] == "Naporia":
        if direction == "go back":
            player["location"] = "Halivaara"
    elif player["location"] == "Wombourne":
        if direction == "go back":
            player["location"] = "Vergamo"
    elif player["location"] == "Sacred Circle":
        if direction == "go back":
            player["location"] = "Wombourne"


# taking/picking up item
def take_item(location_name, item, locations, inventory):
    location = locations[location_name]
    if item in location["items"]:
        inventory.append(item)
        location["items"].remove(item)
        print(f"You pick up the {item}")
    else:
        print(f"There is no {item} here.")

# check for the completion/fail of the game.
def check_end_game(current_location, inventory):
    if current_location == "Sacred Circle":
        if inventory.count("crystal") == 8:
            print("The crystals you have collected appear to have indents where they connect like a puzzle.")
            print("You complete the puzzle and place the giant crystal on the pedestal.")
            print("A portal appears and you walk through it. You have completed the game.")
            print("THE END")
            return True
        else:
            print("You need 8 crystals to place on the pedestal")
    if current_location == "Path" and "Sword" in inventory:
        print("You're ambushed by a group of enemies. You try and fight back. You fail.")
        print("Ending: Ambushed")
        return True
    return False