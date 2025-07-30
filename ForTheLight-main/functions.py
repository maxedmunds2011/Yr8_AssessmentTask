# functions.py
import os
import sys

from colorama import init, Fore, Style
init(autoreset=True)

import shared
import random
from data import Elissus_Rooms, enemy_stats

enemy = None
enemy_health = None
enemy_name = "Crimson Rat"
enemy_drops = None

def show_location(room_name, rooms):
    room = rooms[room_name]
    print("\nYou are in", room_name.upper())
    print(room["description"])
    if room["items"]:
        print("You see:", ", ".join(room["items"]))
    print("Exits:", ", ".join(room["exits"].keys()))

def get_command():
    return input("\nWhat do you do? ").strip().lower()

def move(current_room, direction, rooms):
    if direction in rooms[current_room]["exits"]:
        return rooms[current_room]["exits"][direction]
    else:
        print("You can't go that way.")
        return current_room

def take_item(room_name, item, rooms, inventory):
    room = rooms[room_name]
    if item in room["items"]:
        inventory.append(item)
        room["items"].remove(item)
        print(f"You took the {item}.")
    else:
        print(f"There is no {item} here.")

def check_end_game(current_room, inventory):
    if current_room == "escape_pod":
        if "keycard" in inventory:
            print("You insert the keycard. The pod launches. You’ve escaped!")
            print("ENDING: FREEDOM")
            return True
        else:
            print("You need a keycard to launch the escape pod.")
    if current_room == "hallway" and "blaster" in inventory:
        print("You’re spotted by a patrol droid. You fire!")
        print("ENDING: GUNFIGHT IN THE HALLWAY")
        return True
    return False






def enemies():
    shared.player["location"] = "sewer_depths"
    if shared.player["location"] == "sewer_depths":
        enemy_name = "Crimson Rat"
        return "Crimson Rat"
    return None



def battle_system(enemy):
    enemy = enemies()
    enemy_knowledge = enemy_stats["enemy_data"][enemy_name]
    print("The battle begins!")
    print(f"You encounter a {enemy}!")
    enemy_health = random.choice(enemy_knowledge["health"])
    print(f"{enemy_name} has {enemy_health} health.")
    enemy_drops = random.choice(enemy_knowledge["drops"])
    print(f"The enemy drops {enemy_drops}.")

battle_system(enemy)

def directional_choices(direction):
    
    if shared.player is None:
        return "No player found."


    if shared.player["location"] == "your_room":
        if direction == 'w':
            return "town_street"
        elif direction == 'a':
            return "your_wardrobe"
        else:
            print("You can't go that way.")

    elif shared.player["location"] == "your_wardrobe":
        if direction == 'w':
            return "town_street"
        else:
            print("You can't go that way.")

    elif shared.player["location"] == "town_street":
        if direction == 'a':
            return "harraxx_house"
        elif direction == 'd':
            return "market_square"
        else:
            print("You can't go that way.")

    elif shared.player["location"] == "harraxx_house":
        if direction == 's':
            return "town_street"
        else:
            print("You can't go that way.")
    elif shared.player["location"] == "market_square":
        if direction == 'w':
            return "portal_gate"
        elif direction == 'a':
            return "elder_house"
        elif direction == 'd':
            return "playing_area"
        else:
            print("You can't go that way.")

    elif shared.player["location"] == "elder_house":
        if direction == 's':
            return "market_square"
        else:
            print("You can't go that way.")

    elif shared.player["location"] == "playing_area":
        if direction == 's':
            return "market_square"
        else:
            print("You can't go that way.")

    elif shared.player["location"] == "portal_gate":
        if direction == 's':
            return "market_square"
        elif direction == 'w':
            return "elissus_portal"
        else:
            print("You can't go that way.")
    elif shared.player["location"] == "sewer_depths":
        if direction == 'up':
            return "sewer_end"
        else:
            print("You can't go that way.")

    return None