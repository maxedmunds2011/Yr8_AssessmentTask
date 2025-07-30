
from data import Elissus_Rooms 
import shared
from functions import directional_choices


shared.player = {
        "name": "",
        "progress": 0,
        "player_health": 100,
        "player_dmg": 0,
        "player_def": 0,
        "currency": 0,
        "location": "your_room",
    }

from colorama import init, Fore, Style
init(autoreset=True)  # Resets colour after each print


def start_room():
    starting_room = "your_room"

def main():
    

    start_room()
    current_room = start_room
    print("Current room:", current_room)
    

    items = []

    print ("Only the stars may tell this story.")
    print ("For as long as anyone can remember, there have been five planets.")
    print (Fore.GREEN + "Elissus, Planet of Fertility.")
    print (Fore.BLUE + "Fragira, Planet of Mystery.")
    print (Fore.MAGENTA + "Chystalv, Planet of Weather.")
    print (Fore.CYAN + "Nolox, Planet of Technology.")
    print (Fore.YELLOW + "And Varunii, Planet of Light.")

    print ("The only way to cross between them is when they align...")
    print ("And for all five to align, it takes a milennia.")
    print (Style.BRIGHT + Fore.YELLOW + "Welcome...to The Final Alignment")
    print ("...")

    shared.player ["name"] = input("What is your name? ").strip()
    print(f"Welcome, {shared.player['name']}.")
    open_menu = input("Press 'Enter' to start the game. Type 'z' to check the controls. Type 'c' to check progress.").lower()

    if open_menu == "":
        current_location = "your_room"
        

    elif open_menu == "z":

        print("Controls:")
        print("Use the arrow keys to move.")
        print("Press 'Enter' to interact with objects.")
        print("Press 'Esc' to pause the game.")
        print("Type 'c' to check your progress at any time.")
        open_menu = input("Press 'Enter' to start the game. Type 'z' to check the controls. Type 'c' to check progress.").lower()


    elif open_menu == "c":
        print("Progress:")
        print(f"Your current progress is {shared.player ['progress']}%")
        open_menu = input("Press 'Enter' to start the game. Type 'z' to check the controls. Type 'c' to check progress.").lower()


    else:
        open_menu = input("Press 'Enter' to start the game. Type 'z' to check the controls. Type 'c' to check progress.").lower()

    if current_location == "your_room":
        print(Elissus_Rooms[current_location]["description"])
        command = input(Elissus_Rooms[current_location]["choice"]).lower()
        if command in ['w', 'a', 's', 'd']:
            print(f"DEBUG: Current location before move = {shared.player['location']}")
            shared.player["location"] == directional_choices(command)
            print(f"DEBUG: Current location after move = {shared.player['location']}")
           
        else:
            print("Invalid command. Please try again.")
            command = input(Elissus_Rooms["your_room"]["choice"]).lower()

    if current_location == 'your_wardrobe':
        print(Elissus_Rooms["your_wardrobe"]["description"])
        shared.player ["currency"] += 5
            
    elif current_location == 'town_street':
        location = input().lower()
        
        if street_choice1 == 'a':
            print()
            shared.player ["currency"] += 10
            print("You thank him and head down the street.")
            street_choice1 = 's'
        elif street_choice1 == 's':
            print()
            street_choice2 = input().lower()
        else:
            print("Invalid command. Please try again.")
    else:
        print("Invalid command. Please try again.")
        
main()