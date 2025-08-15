# functions.py

from colorama import Fore, Style
from config import *
import random
from data import *
import sys
import os
import time

completion = True
completion2 = True
completion3 = True

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate(text, delay = 0.04):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def coloured (text, colour=''):
    colours = {
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'grey': '\033[90m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'red': '\033[38;5;196m',
        'default': '\033[0m'
    }
    return f"{colours.get(colour, '')}{text}{colours['default']}"

def start_game():
        animate("Only the stars may tell this story.")
        animate("For as long as anyone can remember, there have been five planets.")
        animate(coloured ('Elissus, Planet of Fertility.', 'green'))
        animate(coloured ('Fragira, Planet of Mystery.', 'blue'))
        animate(coloured ('Chystalv, Planet of Weather.', 'magenta'))
        animate(coloured ('Nolox, Planet of Technology.', 'cyan'))
        animate(coloured ('And Varunii, Planet of Light.', 'yellow'))
        print ("The only way to cross between them is when they align...")
        print ("And for all five to align, it takes a milennia.")
        print (Style.BRIGHT + Fore.YELLOW + "Welcome...to The Final Alignment")
        print ("...")

        p_name = input("What is your name? ").strip()
        print(f"Welcome, {p_name}.")


    

def start_room():
    starting_room = "your_room"
    return starting_room

def check_instructions():
    print("Controls:")
    print("Use the arrow keys to move.")
    print("Press 'Enter' to interact with objects.")
    print("Press 'Esc' to pause the game.")
    print("Type 'c' to check your progress at any time.")

def check_progress():
    print("Progress:")
    print(f"Your current progress is {p_progress}%")


def directional_choices(direction, current_location):
    if current_location == "your_room":
        if direction == 'w':
            return "town_street"
        elif direction == 'a':
            return "your_wardrobe"
        else:
            print("You can't go that way.")
    elif current_location == "your_wardrobe":
        if direction == 's':
            return "your_room"
        else:
            print ("You can't go that way.")
    elif current_location == "town_street":
        if direction == 'd':
            return "market_square"
        else:
            print("You can't go that way.")
    elif current_location == "market_square":
        if direction == 'w':
            return "portal_gate"
        else:
            print("You can't go that way.")
    elif current_location == "portal_gate":
        if direction == 'w':
            return "elissus_portal"
        else:
            print("The only way is forward...")
    elif current_location == "elissus_portal":
        if direction == 'w':
            return "sewer_depths"
        else:
            print ("You can't go that way.")
    elif current_location == "sewer_depths":
        if direction == 'w':
            return "sewer_end"
        else:
            print("You can't go that way.")
    elif current_location == "sewer_end":
        if direction == 'w':
            return "Crimson_streets"
        else:
            print ("You can't go that way.")
    elif current_location == "Crimson_streets":
        if direction == 'w':
            return "broken_portal"
        elif direction == 'a':
            return "elissus_tower"
        elif direction == 'd':
            return "rat_den"
        else:
            print ("You cannot head back now.")
    elif current_location == "elissus_tower":
        if direction == 'w':
            return "towertop"
        elif direction == 's':
            return "Crimson_streets"
        elif direction == 'a':
            return "elissus_puzzle_room"
        else:
            print ("You can't go that way.")
    elif current_location == "elissus_puzzle_room":
        if direction == 's':
            return "elissus_tower"
        else:
            print ("You can't go that way.")
    elif current_location == "towertop":
        if direction == 's':
            return "elissus_tower"
        else:
            print ("You can't go that way.")
    elif current_location == "rat_den":
        if direction == 's':
            return "Crimson_streets"
        else:
            print ("You can't go that way.")
    elif current_location == "broken_portal":
        if direction == 'w':
            return "Torn Landing Pad"
        else:
            print ("You can't go that way.")
    elif current_location == "Torn Landing Pad":
        if direction == 'w':
            return "Elevator"
        else:
            print ("You can't go that way.")
    elif current_location == "Elevator":
        if direction == 'w':
            return "Southern Camp"
        else:
            print ("You can't go that way.")
    elif current_location == "Southern Camp":
        if direction == 'w':
            return "The Maw"
        else:
            print ("You can't go that way.")
    elif current_location == "The Maw":
        if direction == 'w':
            return "Lower Labs"
        elif direction == 'a':
            return "River East"
        elif direction == 's':
            return "Southern Camp"
        else:
            print ("You can't go that way.")
    elif current_location == "Elevator Depths":
        if direction == 'w':
            return "Majestical Clearing"
        else:
            print ("You can't go that way.")
    elif current_location == "River East":
        if direction == 'w':
            return "River West"
        elif direction == 's':
            return "The Maw"
        else:
            print ("You can't go that way.")
    elif current_location == "Majestical Clearing":
        if direction == 'w':
            return "Lower Labs"
        elif direction == 'd':
            return "River West"
        else: 
            print ("You can't go that way.")
    elif current_location == "River West":
        if direction == 'w':
            return "River East"
        elif direction == 's':
            return "Majestical Clearing"
        else:
            print ("You can't go that way.")
    elif current_location == "Lower Labs":
        if direction == 'w':
            return "Singularity Lab"
        else:
            print ("You can't go that way.")
    elif current_location == "Singularity Lab":
        if direction == 'w':
            return "Crystal Delta"
        elif direction == 'd':
            return "Crystal Omega"
        else:
            print ("You can't go that way.")
    return None

def weapon_allowed(current_location):
    weapon_name1 = "Blunt Knife"
    if current_location == "sewer_depths" and weapon_name1 not in weapons:
        weapons.append(weapon_name1)

def enemies(current_location):
    if current_location == "sewer_depths":
        return "Crimson Rat"
    elif current_location == "rat_den":
        return "Crimson Rats"
    elif current_location == "elissus_tower":
        return "Living Statue"
    elif current_location == "Elevator":
        return "Fragmented Husk"
    elif current_location == "Southern Camp":
        return "Mysterious Soldier"
    elif current_location == "The Maw":
        return "Winged Crimsons"
    elif current_location == "Lower Labs":
        return "Mad Scientist"
    return None



def puzzles(current_location):
    global completion, completion2, defences, p_location, p_health, completion3

    if p_location == "elissus_puzzle_room" and completion == True:
        print("The stone hums with energy. It recites 'In order of planets, what is the fourth planet?'")
        print("1 - Elissus")
        print("2 - Fragira")
        print("3 - Nolox")
        print("4 - Varunii")
        puzzle = input("Enter here (1, 2, 3, 4): ")
        if puzzle == "3":
            if "Farmer Tunic" not in defences:
                defences.append("Farmer Tunic")
            print("That's correct! You gained the Farmer Tunic!")
            completion = False

    elif p_location == "towertop" and completion2 == True:
        print("A riddle is written in the middle. It recites: '10, 12, 16, 24, 40. What is the next in this pattern?'")
        print("1 - 72")
        print("2 - 48")
        print("3 - 104")
        print("4 - 75")
        puzzle = input("Enter here (1, 2, 3, 4): ")
        if puzzle == "1":
            print("You answered correctly!")
            completion2 = False
        else:
            print("Wrong answer. You lose 20 HP.")
            p_health -= 20

    elif p_location == "Lower Labs" and completion3 == True:     
        print("A riddle is written next to the door. It recites 'Fill in the blank. When the light is subsumed in dark, the saviour shall illuminate the ____'.")
        print("1 - might")
        print("2 - stars")
        print("3 - mark")
        print("4 - harp")
        puzzle = input("Enter here (1, 2, 3, 4): ")
        if puzzle == "2":
            print("You answered correctly!")
            completion3 = False
        else:
            print("Wrong answer. You lose 25 HP.")
            p_health -= 25

def battle_system(current_location):
    global p_health, p_max_health, weapons, abilities, items, defences, current_defences
    weakness = False
    weakness1 = 0
    weakness2 = False
    weakness3 = False
    weakness4 = False
    weakness5 = False
    weakness6 = False
    break_allowed = False
    NPC_scientist = True


    enemy = enemies(current_location)
    if not enemy:
        print("No enemy here!")
        return

    def enemy_weaknesses():
        if enemy == "Crimson Rat" and weakness == True:
            break_allowed = True
            weakness = False
        if enemy == "Crimson Rats" and weakness1 == 2:
            break_allowed = True
            weakness1 = False
        if enemy == "Living Statue" and weakness2 == True:
            break_allowed = True
            weakness2 = False
        if enemy == "Fragmented Husk" and weakness3 == True:
            enemy_health -= 50
            weakness3 = False
        if enemy == "Mysterious Soldier" and weakness4 == True:
            break_allowed = True
            weakness4 = False
        if enemy == "Winged Crimsons" and weakness5 == True:
            p_max_health += 20
            weakness5 = False
        if enemy == "Mad Scientist" and weakness6 == True:
            NPC_scientist = True
            break_allowed = True
            weakness6 = False



    enemy_weaknesses()
    enemy_name_local = enemy
    enemy_health = random.choice(enemy_stats["enemy_data"][enemy_name_local]["health"])
    print("The battle begins!")
    print(f"You encounter a {enemy}!")
    print(f"{enemy_name_local} has {enemy_health} health.")
    heal_times = 0
    halved_dmg = False

    def enemy_take_damage(damage):
        nonlocal enemy_health
        enemy_health -= damage

    while enemy_health > 0 and p_health > 0:
        print("Your turn!")
        battle_choice = input("What do you do? To use an ability, type 'a'. To attack, type 'x'. To use an item, type 'i'. To check the enemy's stats, type 's'. To heal, press 'h'.").lower()

        if battle_choice == 'a':
            print(f"Your current abilities are: {abilities}")
            ability = input(f"Type the name of the ability you want to use: ").capitalize()
            if ability in abilities:
                if ability == "Growth":
                    heal_amount = 15
                    p_health = min(p_max_health, p_health + heal_amount)
                    print(f"Your current health is {p_health}")
            else:
                print("You don't have that ability.")

        elif battle_choice == 'x':
            weapon_allowed(current_location)
            print(f"Your current weapons are: {weapons}")
            weapon_choice = input(f"What weapon shall you use? ")
            if weapon_choice in weapons:
                if halved_dmg:
                    player_damage_amount = random.choice(weapon_stats[weapon_choice]["damage"]) // 2
                    halved_dmg = False
                else:
                    player_damage_amount = random.choice(weapon_stats[weapon_choice]["damage"])
                enemy_take_damage(player_damage_amount)
                print(f"You use your {weapon_choice} and deal {player_damage_amount} damage!")
                print(f"Enemy health: {enemy_health}")
            else:
                print("You don't have that weapon.")

        elif battle_choice == 'i':
            print(f"Your current items are: {items}")
            item = input("What item will you use? ")
            if item in items:
                if item == "Festival Bouquet":
                    print("Nothing happens")
                elif item == "Blessed Carrot":
                    heal_amount = 999
                    p_health = min(p_max_health, p_health + heal_amount)
                    print("You replenished all health!")
            else:
                print("You don't have that item.")

        elif battle_choice == 's':
            print(f"{enemy_stats['enemy_data'][enemy_name_local]}")

        elif battle_choice == 'h':
            if heal_times == 0:
                print("Next turn, your damage will be decreased")
                halved_dmg = True
                print("You heal 30HP.")
                heal_amount = 30
                p_health = min(p_max_health, p_health + heal_amount)
                print(f"Your current health is {p_health}")
                heal_times += 1
            else:
                print("You've used all heals.")

        else:
            print("Invalid type. Miss a turn!")

        if enemy_health <= 0:
            print("You win the battle!")
            return "Victory"

        print("Enemy turn!")
        print(f"The {enemy_name_local} attacks!")

        def take_damage():
            global p_health
            raw_damage_amount = (enemy_stats["enemy_data"][enemy_name_local]["damage"])
            if current_defences:
                defence_val = max(defence_stats[d]["defence"] for d in current_defences if d in defence_stats)
            else:
                defence_val = 1
            enemy_damage_amount = random.choice(raw_damage_amount)
            true_enemy_damage = max(0, enemy_damage_amount - defence_val)
            p_health = (p_health - true_enemy_damage)
            print(f"The {enemy_name_local} deals {true_enemy_damage} damage!")
            print(f"Player health: {p_health}")
        take_damage()

        if p_health <= 0:
            print("You have been defeated!")
            return "Defeat"
        
        if break_allowed == True:
            return "Victory"

import json

def save_game(state, filename="savefile.json"):
    with open(filename, "w") as f:
        json.dump(state, f, indent=4)
    print("Game saved.")

def load_game(filename="savefile.json"):
    try:
        with open(filename, "r") as f:
            state = json.load(f)
        print("Game loaded.")
        return state
    except FileNotFoundError:
        print("No save file found.")
        return None
    
def inventory_system():
    inventory_check = True
    while inventory_check == True:

        print (f"Your current items are: {items}")
        print (f"Your current weapons are: {weapons}")
        print (f"Your current defences are: {defences}")
        print (f"Your current abilities are: {abilities}")

        print ("To check an item, type '1'")
        print ("To check a weapon, type '2'")
        print ("To check a defence, type '3'")
        print ("To check an ability, type '4'")

        check = input ("Enter 1, 2, 3 or 4 depending on what you want to check, or press any other to exit.")
        if check == "1":
            print (items)
            check_items = input ("What item would you like to check?")
            if check_items in items:
                animate (item_stats[check_items]["description"])
                continue
            else:
                print ("You don't have that item.")
                continue

        elif check == "2":
            print (weapons)
            check_weapons = input ("What weapon would you like to check?")
            if check_weapons in weapons:
                animate (weapon_stats[check_weapons]["description"])
                continue
            else:
                print ("You don't have that weapon.")
                continue

        elif check == "3":
            print (defences)
            check_defences = input ("What defence would you like to check?")
            if check_defences in defences:
                animate (defence_stats[check_defences]["description"])
                continue
            else:
                print ("You don't have that defence.")
                continue

        elif check == "4":
            print (abilities)
            check_abilities = input ("What ability would you like to check?")
            if check_abilities in abilities:
                animate (ability_stats[check_abilities]["description"])
                continue
            else:
                print ("You don't have that ability.")
                continue

        else:
            print ("Thank you for using the inventory system")
            break
    inventory_check = False

loaded_state = load_game()

heal_times = 0
def Elissian_Zero(current_location):
    global p_health, p_max_health, weapons, abilities, items, defences, current_defences
    weapons.append ("Blunt Knife")
    abilities.append ("Growth")
    boss_health = (boss_stats["Harraxx, Elissian Zero"]["health"])
    turn = 1
    def boss_take_damage(damage):
        nonlocal boss_health
        boss_health -= damage

    def boss_round():
        global heal_times, p_health, p_max_health, weapons, abilities, items, defences, current_defences
        print("Your turn!")
        battle_choice = input("What do you do? To use an ability, type 'a'. To attack, type 'x'. To use an item, type 'i'. To check the enemy's stats, type 's'. To heal, press 'h'.").lower()

        if battle_choice == 'a':
            print(f"Your current abilities are: {abilities}")
            ability = input(f"Type the name of the ability you want to use: ").capitalize()
            if ability in abilities:
                if ability == "Growth":
                    heal_amount = 15
                    p_health = min(p_max_health, p_health + heal_amount)
                    print(f"Your current health is {p_health}")
            else:
                print("You don't have that ability.")

        elif battle_choice == 'x':
            weapon_allowed(current_location)
            print(f"Your current weapons are: {weapons}")
            weapon_choice = input(f"What weapon shall you use? ")
            if weapon_choice in weapons:
                if halved_dmg == True:
                    player_damage_amount = random.choice(weapon_stats[weapon_choice]["damage"]) // 2
                    halved_dmg = False
                else:
                    player_damage_amount = random.choice(weapon_stats[weapon_choice]["damage"])
                boss_take_damage(player_damage_amount)
                print(f"You use your {weapon_choice} and deal {player_damage_amount} damage!")
                print(f"Boss health: {boss_health}")
            else:
                print("You don't have that weapon.")

        elif battle_choice == 'i':
            print(f"Your current items are: {items}")
            item = input("What item will you use? ")
            if item in items:
                if item == "Festival Bouquet":
                    print("Nothing happens")
                elif item == "Blessed Carrot":
                    heal_amount = 999
                    p_health = min(p_max_health, p_health + heal_amount)
                    print("You replenished all health!")
            else:
                print("You don't have that item.")

        elif battle_choice == 's':
            animate("This creature has an unknown statistics. Growth may be helpful in this fight...")

        elif battle_choice == 'h':
            if heal_times == 0 or 1:
                print("Next turn, your damage will be decreased")
                halved_dmg = True
                print("You heal 30HP.")
                heal_amount = 30
                p_health = min(p_max_health, p_health + heal_amount)
                print(f"Your current health is {p_health}")
                heal_times += 1
            else:
                print("You've used all heals.")

        else:
            print("Invalid type. Miss a turn!")

        if boss_health <= 0:
            print("Harraxx, the friend you've known for your entire life, is dead in your hands...")
            return "Victory"

        print("Enemy turn!")
        print(f"Harraxx attacks!")

        def take_damage():
            global p_health
            if turn == 1:
                boss_attack = random.choice(list(boss_stats["Harraxx, Elissian Zero"]["attacks1"].keys()))
                boss_dmg = random.choice(boss_stats["Harraxx, Elissian Zero"]["attacks1"][boss_attack]["damage"])
                print (boss_dmg)
            elif turn == 2:
                boss_attack = random.choice(list(boss_stats["Harraxx, Elissian Zero"]["attacks2"].keys()))
                boss_dmg = random.choice(boss_stats["Harraxx, Elissian Zero"]["attacks2"][boss_attack]["damage"])
                print (boss_attack)
            elif turn == 3:
                boss_attack = random.choice(list(boss_stats["Harraxx, Elissian Zero"]["attacks3"].keys()))
                boss_dmg = random.choice(boss_stats["Harraxx, Elissian Zero"]["attacks3"][boss_attack]["damage"])
                print (boss_attack)
            elif turn == 4:
                boss_attack = random.choice(list(boss_stats["Harraxx, Elissian Zero"]["attacks4"].keys()))
                boss_dmg = random.choice(boss_stats["Harraxx, Elissian Zero"]["attacks4"][boss_attack]["damage"])
                print (boss_attack)
            elif turn == 5:
                boss_attack = random.choice(list(boss_stats["Harraxx, Elissian Zero"]["attacks5"].keys()))
                boss_dmg = random.choice(boss_stats["Harraxx, Elissian Zero"]["attacks5"][boss_attack]["damage"])
                print (boss_attack)
            elif turn == 6:
                boss_attack = random.choice(list(boss_stats["Harraxx, Elissian Zero"]["attacks6"].keys()))
                boss_dmg = random.choice(boss_stats["Harraxx, Elissian Zero"]["attacks6"][boss_attack]["damage"])
                print (boss_attack)

            if current_defences:
                defence_val = max(defence_stats[d]["defence"] for d in current_defences if d in defence_stats)
            else:
                defence_val = 1
            boss_damage_amount = random.choice(boss_attack)
            true_boss_damage = max(0, int(boss_damage_amount) - defence_val)
            p_health = (p_health - true_boss_damage)
            print(f"Harraxx uses {boss_attack} and deals {true_boss_damage} damage!")
            print(f"Player health: {p_health}")
        take_damage()

        if p_health <= 0:
            print("You have been defeated!")
            return "Defeat"

    if True:
        while boss_health >= 0 and p_health >= 0 and turn < 8:
            if turn == 1:
                animate (boss_stats["Harraxx, Elissian Zero"]["dialogue"]["1"])
                boss_round()
                turn += 1
                continue
            elif turn == 2:
                animate (boss_stats["Harraxx, Elissian Zero"]["dialogue"]["2"])
                boss_round()
                turn += 1
                continue
            elif turn == 3:
                animate (boss_stats["Harraxx, Elissian Zero"]["dialogue"]["3"])
                boss_round()
                turn += 1
                continue
            elif turn == 4:
                animate (boss_stats["Harraxx, Elissian Zero"]["dialogue"]["4"])
                boss_round()
                turn += 1
                continue
            elif turn == 5:
                animate (boss_stats["Harraxx, Elissian Zero"]["dialogue"]["5"])
                boss_round()
                turn += 1
                continue
            elif turn == 6:
                animate (boss_stats["Harraxx, Elissian Zero"]["dialogue"]["6"])
                boss_round()
                turn += 1
                continue
            elif turn == 7:
                animate (boss_stats["Harraxx, Elissian Zero"]["dialogue"]["7"])
                turn += 1
                continue

print ("Hi")
