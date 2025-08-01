# functions.py
import os
import sys

import shared
import random
from data import Elissus_Rooms, enemy_stats, player_stats, weapon_stats

weapons = []
abilities = []
items = ["Festival Bouquet"]

enemy = None

enemy_name = "Crimson Rat"
enemy_drops = None
enemy_damage_amount = 0
player_damage_amount = 0
heal_amount = 0

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

def weapon_allowed():
    weapon_name1 = "Blunt Knife"
    shared.player["location"] = "sewer_depths"
    if shared.player["location"] == "sewer_depths":
        if weapon_name1 not in weapons:
            weapons.append(weapon_name1)

def enemies():
    shared.player["location"] = "sewer_depths"
    if shared.player["location"] == "sewer_depths":
        enemy_name = "Crimson Rat"
        return "Crimson Rat"
    return None



    




  

def heal_player():
    player_stats["health"] = min(player_stats["max_health"], player_stats["health"] + heal_amount)


def battle_system():

    enemy = enemies()
    enemy_knowledge = enemy_stats["enemy_data"][enemy_name]
    enemy_health = random.choice(enemy_knowledge["health"])
    print("The battle begins!")
    print(f"You encounter a {enemy}!")
    print(f"{enemy_name} has {enemy_health} health.")

    def enemy_take_damage():
        nonlocal enemy_health
        enemy_health -= player_damage_amount 
    while enemy_health > 0 and player_stats["health"] > 0:

        print("Your turn!")
        battle_choice = input("What do you do? To use an ability, type 'a'. To attack, type 'x'. To use an item, type 'i'. To check the enemy's stats, type 's'. To heal, press 'h'.").lower()


        if battle_choice == 'a':
                print(f"Your current abilities are: {abilities}")
                ability = input(f"Type the name of the ability you want to use: ").upper()
                if ability in abilities:
                    if ability == "Growth":
                        heal_amount += 15
                        heal_player()
                        print(f"Your current health is {player_stats["health"]}")
                else:
                    print("You don't have that ability.")


        elif battle_choice == 'x':
                weapon_allowed()
                print(f"Your current weapons are: {weapons}")
                weapon_choice = input(f"What weapon shall you use? ")
                if weapon_choice in weapons:
                    player_damage_amount = random.choice(weapon_stats[weapon_choice]["damage"])

                    enemy_take_damage()
                    print (f"You use your {weapon_choice} and deal {player_damage_amount} damage!")
                    print (f"Enemy health: {enemy_health}")
                else:
                    print("You don't have that weapon.")


        elif battle_choice == 'i':
                print(f"You current items are: {items}")
                item = input("What item will you use?")
                if item in items:
                    if item == "Festival Bouquet":
                        print("Nothing happens")
                else:
                    print("You don't have that item.")


        elif battle_choice == 's':
                print(f"{enemy_stats["enemy_data"][enemy_name]}")


        elif battle_choice == 'h':
                print("Next turn, your damage will be decreased")
                halved_dmg = True
                print("You heal 30HP.")
                heal_amount += 30
                heal_player()
                print(f"Your current health is {player_stats["health"]}")


        else:
            print("Invalid type. Miss a turn!")


        if enemy_health <= 0:
            break




        print("Enemy turn!")
        print(f"The {enemy_name} attacks!")

        def take_damage():
            player_stats["health"] = max(0, player_stats["health"] - enemy_damage_amount)
        enemy_damage_amount = random.choice(enemy_stats["enemy_data"][enemy_name]["damage"])
        take_damage()

        print(f"The {enemy_name} deals {enemy_damage_amount} damage!")
        print(f"Player health: {player_stats["health"]}")


        if player_stats["health"] <= 0:
            break


battle_system()