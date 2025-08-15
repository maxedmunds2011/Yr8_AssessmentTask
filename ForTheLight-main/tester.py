from colorama import Fore, init
init(autoreset=True)
from functions import start_room, start_game, check_instructions, check_progress, animate, coloured, directional_choices, items, battle_system, save_game, load_game, puzzles, inventory_system, loaded_state, Elissian_Zero
from data import *
from config import *


def player_defeat():
    print ("You have been defeated.")
    restart = input ("Would you like to restart? Type y to restart, anything else to leave.")
    if restart == 'y':
        main()
    else:
        print ("Hi")

def main():
    global p_health
    global p_max_health
    global p_name
    global p_progress
    global p_damage
    global p_defence
    global p_currency
    global p_location
    global save_time
    global puzzle1
    global puzzle2
    global battle_fought
    global battle_fought2
    global items
    global weapons
    global abilities
    global defences

    battle_fought = False
    battle_fought2 = False
    save_time = True
    puzzle1 = True
    puzzle2 = True

    start_game()
    open_menu = input("Press 'Enter' to start the game. Type 'z' to check the controls. Type 'c' to check progress.").lower()

    current_location = ""

    if open_menu == "":
        current_location = "your_room"

    elif open_menu == "z":
        from functions import check_instructions
        check_instructions()
        current_location = "your_room"

    elif open_menu == "c":
        from functions import check_progress
        check_progress()
        current_location = "your_room"

    else:
        print("Invalid option. Please try again.")
        current_location = "your_room"

    # Main game loop - handle room interactions
    while True:
        broken_entry = False
        boss_fought = False

        if current_location == "your_room":
            animate(Elissus_Rooms[current_location]["description"])
            command = input(Elissus_Rooms[current_location]["choice"]).lower()
            if command in ['w', 'a', 's', 'd']:
                new_location = directional_choices(command, current_location)
                if new_location:
                    p_location = new_location
                    current_location = new_location
            else:
                print("Invalid command. Please try again.")
                continue

        elif current_location == 'your_wardrobe':
            wardrobe_currency = True
            print(Elissus_Rooms["your_wardrobe"]["description"])
            if wardrobe_currency == True:
                p_currency += 5
                print(f"You found 5 currency! You now have {p_currency} currency.")
                wardrobe_currency = False
            command = input("To head back, type 's'.")
            if command in ['w', 'a', 's', 'd']:
                new_location = directional_choices(command, current_location)
                if new_location:
                    p_location = new_location
                    current_location = new_location    
                
        elif current_location == 'town_street':
            print(Elissus_Rooms["town_street"]["description"])
            street_choice1 = input(Elissus_Rooms["town_street"]["choice"]).lower()
            
            if street_choice1 == 'a':
                print("You approach the friendly stranger.")
                p_currency += 10
                print(f"You received 10 currency! You now have {p_currency} currency.")
                print("You thank him and head down the street.")
            elif street_choice1 == 'd':
                print("You decide to continue down the street.")
            else:
                print("Invalid choice. Please try again.")
                continue
            
            # After town street interaction, allow further movement
            command = input(Elissus_Rooms[current_location]["choice"]).lower()
            if command in ['w', 'a', 's', 'd']:
                new_location = directional_choices(command, current_location)
                if new_location:
                    p_location = new_location
                    current_location = new_location    
            
        
        elif current_location == "market_square":
            print(Elissus_Rooms["market_square"]["description"])
            street_choice_2 = input(Elissus_Rooms["market_square"]["choice"]).lower()

            if street_choice_2 == 'a':
                print(Elissus_Rooms["elder_house"]["description"])
                print(Fore.YELLOW + "You got the Festival Bouquet! You put it in your inventory.")
                items.append("Festival Bouquet")

                street_choice_3 = input("To talk to the kids, go down. To continue along the street, go right. ('s' or 'd')").lower()
                if street_choice_3 not in ['s', 'd']:
                    print("Invalid command. Try again.")
                    continue
                elif street_choice_3 == 's':
                    print(Elissus_Rooms["playing_area"]["description"])
                elif street_choice_3 == 'd':
                    print("You continue along the street.")

            elif street_choice_2 == 'd':
                print(Elissus_Rooms["playing_area"]["description"])

                street_choice_4 = input("To head back to Aksovv, go back. To continue along the street, head left. ('s' or 'a')").lower()
                if street_choice_4 not in ['s', 'a']:
                    print("Invalid command. Try again.")
                    continue
                elif street_choice_4 == 's':
                    print(Elissus_Rooms["elder_house"]["description"])
                    print(Fore.YELLOW + "You got the Festival Bouquet! You put it in your inventory.")
                    items.append("Festival Bouquet")
                elif street_choice_4 == 'a':
                    print("You continue along the street.")

            elif street_choice_2 == 'w':
                print("You make your way further down the street.")

            else:
                print("Invalid command. Try again.")
                continue
            
            command = input ("Press 'w' to continue.").lower()
            if command == 'w':
                new_location = directional_choices(command, current_location)
                if new_location:
                    p_location = new_location
                    current_location = new_location


        elif current_location == "portal_gate":
            print (Elissus_Rooms[current_location]["description"]) 
            command = input(Elissus_Rooms[current_location]["choice"]).lower()
            if command in ['w', 'a', 's', 'd']:
                new_location = directional_choices(command, current_location)
                if new_location:
                    p_location = new_location
                    current_location = new_location
                    

        elif current_location == "elissus_portal":
            print (Elissus_Rooms[current_location]["description"])
            command = input ("Press 'w' to continue.").lower()
            if command == 'w':
                new_location = directional_choices(command, current_location)
                if new_location:
                    p_location = new_location
                    current_location = new_location

        elif current_location == "sewer_depths":
            print (Elissus_Rooms[current_location]["description"])
            weapons.append ("Blunt Knife")
            outcome = battle_system(current_location)
            if outcome == "Victory":
                print ("Good job.")
                current_location = None
                current_location = "sewer_end"
            elif outcome == "Defeat":
                player_defeat()
            command = input (Elissus_Rooms[current_location]["choice"])
            if command in ['w', 'a', 's', 'd']:
                new_location = directional_choices(command, current_location)
                if new_location:
                    p_location = new_location
                    current_location = new_location

        elif current_location == "sewer_end":
            print (Elissus_Rooms[current_location]["description"])
            abilities.append (Elissus_Rooms[current_location]["abilities"])
            command = input (Elissus_Rooms[current_location]["choice"])
            if command in ['w', 'a', 's', 'd']:
                new_location = directional_choices(command, current_location)
                if new_location:
                    p_location = new_location
                    current_location = new_location 

        elif current_location == "Crimson_streets":
            animate (Elissus_Rooms[current_location]["description"])
            if save_time == True:
                # Define the current game state to save
                state = {
                    "p_health": p_health,
                    "p_max_health": p_max_health,
                    "p_name": p_name,
                    "p_progress": p_progress,
                    "p_damage": p_damage,
                    "p_defence": p_defence,
                    "p_currency": p_currency,
                    "p_location": p_location,
                    "items": items,
                    "abilities": abilities,
                    "weapons": weapons
                }
                save_game(state)
                save_time = False
            inventory_choice = input(Elissus_Rooms[current_location]["save_point"])
            if inventory_choice == 'i':
                inventory_system()
            command = input (Elissus_Rooms[current_location]["choice"])
            if command in ['w', 'a', 's', 'd']:
                new_location = directional_choices(command, current_location)
                if new_location:
                    p_location = new_location
                    current_location = new_location 
        
        elif current_location == "rat_den":
            animate (Elissus_Rooms[current_location]["description"])
            if battle_fought == False:
                outcome = battle_system(current_location)
                if outcome == "Victory":
                    print ("You won the battle!")
                    battle_fought == True
                else:
                    player_defeat()
            animate ("Defeating the rats, you find the Blessed Carrot! Your Blessed Carrot is put in your items.")
            items.append ("Blessed Carrot")
            command = input (Elissus_Rooms[current_location]["choice"])
            if command == '':
                new_location = directional_choices(command, current_location)
                if new_location:
                    p_location = new_location
                    current_location = new_location 

        elif current_location == "elissus_tower":
            animate (Elissus_Rooms[current_location]["description"])
            command = input (Elissus_Rooms[current_location]["choice"])
            if command in ['w', 'a', 's', 'd']:
                new_location = directional_choices(command, current_location)
                if new_location:
                    p_location = new_location
                    current_location = new_location

        elif current_location == "elissus_puzzle_room":
            while True:
                animate(Elissus_Rooms[current_location]["description"])
                puzzles(current_location)
                command = input(Elissus_Rooms[current_location]["choice"])
                if command in ['w', 'a', 's', 'd']:
                    new_location = directional_choices(command, current_location)
                    if new_location and new_location != current_location:
                        p_location = new_location
                        current_location = new_location
                        break  # Exit the puzzle room loop
                else:
                    print("Invalid command. Please try again.")
            continue

        elif current_location == "towertop":
            while True:
                animate(Elissus_Rooms[current_location]["description"])
                puzzles(current_location)
                broken_entry = True
                command = input(Elissus_Rooms[current_location]["choice"])
                if command in ['w', 'a', 's', 'd']:
                    new_location = directional_choices(command, current_location)
                    if new_location and new_location != current_location:
                        p_location = new_location
                        current_location = new_location
                        break  # Exit the puzzle room loop
                else:
                    print("Invalid command. Please try again.")
            continue

        elif current_location == "broken_portal":
            if broken_entry == False:
                animate ("The gate forbids you from currently entering.")
                current_location = "Crimson_streets"
            elif broken_entry == True:
                animate ("With the gate open, you make your way into the courtyard. There is Harraxx, writing in agony. Blood pours out of him as his head cracks. Your friend has become the first infected human. And death is in his eyes...")
                if boss_fought == False:
                    outcome = Elissian_Zero(current_location)
                    if outcome == "Victory!":
                        boss_fought = True
                    elif outcome == "Defeat":
                        player_defeat()
                animate ("After the body hits the ground, a holy figure materialises in the sky and faces you. A god. 'You have done well thus far. The creature that is following you is bloodthirsty. They were once one of us. Not anymore. Here. I give you a relic that will help create the legendary weapon. Good luck...and remember your powers.'")
                print ("You gained the Fertility Tome!" + Fore.YELLOW)


        else:
            print(f"Location '{current_location}' not implemented yet.")
            break

print ("You gained the Fertility Tome!" + Fore.YELLOW)
main()