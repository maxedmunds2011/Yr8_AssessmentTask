#libraries
import random #used for odds 
import os #hopefully this doesnt crash because im using mac (it didnt crash)
import time #used for time.sleep, which is used to make the game have have pauses at times, so it is easier to read an follow
import math #used for math.ceil, which is used to calculate the wild level of the dragon you encounter

#variable and list setting
inventory = { 
    "Cow carcass": 1,
    "Training manual": 2,
    "Health potion": 2
} #inventory is a dictionary that stores items and their quantities
dragons = [] #dragons is a list to store players dragons, probably have multiple dictionaries in it, each representing a dragon
max_wild_level = 7 #Sets max level which a wild dragon can be, it will increase incrementally as you win battles
max_player_level = 7 #sets max level which a player can be, it will increase incrementally as you win battles


def clear_screen():
    if os.name == 'nt':  # Windows version of the command
        os.system('cls')
    else:  # macOS/Linux/others version of the command
        os.system('clear')

def main_menu(): #outputs a value which is used to decide what happens next
    clear_screen() #uses the clear_screen function to clear screen
    print("Pick an option to perform") 
    print("1. Explore")
    print("2. View Inventory")
    print("3. View Dragons")
    print("4. Exit") #prints the main menu options
    try: #i use this funtion multiple times throught the code, which prevents the program from breaking if the user puts in an invalid input
        menu_choice = int(input("Input your choice:\n")) 
    except ValueError: #second part of the try funtion
        menu_choice = 0
    return menu_choice #returns the user's choice to the main gameloop

def explore(): #the explore funtion
    while True: #loop that keeps the player to keep exploring until they find something or choose to return home
        global inventory
        clear_screen()
        print("Exploring...")
        time.sleep(1)
        destination = random.randint(1, 70) #picks a random number between 1 and 70 which decides what will happen when the player explores
        if destination in range(1, 10): #1 in 7 odds that you find a cow carcass
            print("Found a cow carcass.")
            inventory["Cow carcass"] += 1
        elif destination in range(11, 21): #1 in 7 odds that you find a training manual
            print("Found a training manual.")
            inventory["Training manual"] += 1
        elif destination in range(21, 31): #1 in 7 odds that you find a health potion
            print("You found a potion of healing")
            inventory["Health potion"] += 1
        elif destination in range(31, 51): #2 in 7 odds that you find a dragon
            print("Found dragon.")
            dragon_found()
            return
        elif destination in range(51, 71): #2 in 7 odds that you find nothing
            print("Found nothing, Explore again?")
            print("1. Yes, explore again")
            print("2. No, return home")
            choice = input("Your choice:\n ")
            if choice == '1': #if the user chooses to explore again, the loop continues
                continue
            else:
                break
        break

def view_inventory(): #the view inventory function
    clear_screen()
    print("Length:", len(inventory)) #prints the length of the inventory
    print("Items:")
    for i, (item, quantity) in enumerate(inventory.items(), start=1): # enumerate is used to get the index and the item in the inventory
        print(f"{i}. {item}, Quantity: {quantity}") #prints items and the quantity, using a dictionary that is selected via the for loop above
    input("Press Enter to continue...\n") #allows player to input anything to continue, this is used multiple times throughout the code to make the game easier to follow

def create_dragon(name, level, move, max_damage): #this funtion creates a dragon, this time actually using parameters within the brackets of the function
    return {
        "name": name,
        "level": level,
        "hp": level * 10,
        "move": move,
        "max_damage": max_damage #used to add dragon to the dragons list dictionary
    }

def dragon_found(): #continuing on from the explore function, this function is used when a dragon is found
    global max_wild_level, wild_enemy #allows the function to edit and acces variables outside of the function
    clear_screen() #clears the screen
    wild_level = (max_wild_level - math.ceil(max_wild_level/random.randint(4, 8 ))) #calculates the level of a wild dragon, ranging from 3/4 of the max wild level to the max wild level
    wild_hp = (wild_level*10) #hp always is 10 times the level of the dragon
    wild_damage = (max(1, int(wild_hp * 0.3))) #damage is 30% of the hp, unlress the hp is less than 1, then it is set to 1
    #creates a dictionary for the wild enemy, which is used in the battle function
    wild_enemy = {
        "name": "Wild Dragon",
        "level": wild_level,
        "hp": wild_hp,
        "max_damage": wild_damage
    }

    print(f"Name: {wild_enemy["name"]} | Level: {wild_enemy['level']} | HP: {wild_enemy['hp']} | Max Damage: {wild_enemy['max_damage']}") #Does some fancy printing stuff to display the dragons stats
    print("Would you like to")
    print("1: Fight")
    print("2: Flee")
    choice = str(input("Enter Choice: \n")) #normal choice input, different from the try function because there will not be a value error, as a string can be anything (wanted to try someting different)
    if choice == "1":
        battle()
    else: #i dont care if you selected 2 or if you typed hair toes, if its not 1, you flee.
        print("Returning to main menu")
        return
    

def battle(): #the battle funtion

    global inventory, dragons, wild_enemy, max_wild_level, max_player_level #uses gobal variables again.
    clear_screen()
    print("Chose your dragon")
    for i, dragon in enumerate (dragons, start=1): #uses the enumerate thing i used earlier, to print the dragons list dictionary.
        print(f"{i}: Name: {dragon["name"]} | Level: {dragon["level"]} | Move: {dragon["move"]} | Max Damage: {dragon["max_damage"]}") #actually prints it
    try: #we know what this does
        choice = int(input("Enter your choice:\n ")) - 1 #subtracts one due to the fact that coding always starts at 0, but the list when printed starts at 1
    except ValueError:
        print("Invalid input.")
        return
    if choice < 0 or choice >= len(dragons): #checks if the choice is valid
        print("Invalid choice.")
        return

    player_dragon = dragons[choice] #creates a dictionary based on the choice of dragon from the player

    if inventory["Cow carcass"] < 1: #if you dont have a cow carcass, it asks if you want to continue anyway 
        print("You dont have any Cow Carcasses to tame the dragon.")
        print("Continue anyway?")
        print("1: Yes")
        print("2: No")
        if input("Enter Choice:\n ") == "2": 
            return

    enemy_hp = wild_enemy['hp'] #sets the enemy hp to the wild enemy's hp
    player_hp = player_dragon['hp'] #sets the player hp to the player's dragon hp
    print("Prepare for battle!")
    turn = 1
    while player_hp > 0 and enemy_hp > 0: #while both the player and enemy have hp, the battle continues
        while turn == 1: #during the player's turn:
            clear_screen()
            print("Your turn!")
            print(f"Your HP: {player_hp}") #prints the player's hp
            print(f"Enemy HP: {enemy_hp}") #prints the enemy's hp
            print(f"Your Dragon: {player_dragon['name']} | Level: {player_dragon['level']} | Move: {player_dragon['move']} | Max Damage: {player_dragon['max_damage']}") #prints the player's dragon's stats
            print(f"Enemy Dragon: {wild_enemy['name']} | Level: {wild_enemy['level']} | HP: {wild_enemy['hp']} | Max Damage: {wild_enemy['max_damage']}") #prints the enemy's dragon's stats
            print("What would you like to do?")
            print("Options: ")
            print("1: Attack")
            print("2: Heal (uses potion if available)")
            print("3: Flee")
            choice = int(input("Enter Choice: \n")) #choice = input from player
            
            try: #using the try funtion again for some reason instead of the string statement... dont know why
                if choice == 1: 
                    clear_screen()
                    damage = random.randint(int(player_dragon["max_damage"] * 0.8), int(player_dragon["max_damage"])) #calculates the player's damage, ranging from 80% to 100% of the max damage
                    enemy_hp -= damage #subtracts the damage from the enemy's hp
                    print("Nice Hit!!") 
                    print(f"You dealt {damage} damage, which was {int(damage / player_dragon["max_damage"] * 100)}% of your max damge.") #does some math to show the player how much damage they dealt
                    if enemy_hp < 0: #makes sure the enemy's hp does not go below 0
                        enemy_hp = 0
                    print(f"Enemy hp remaining: {enemy_hp}.") #prints remaining enemy hp
                    input("Press enter to continue: \n")
                    turn = 2
                if choice == 2: #if healtph potion is selected
                    clear_screen()
                    
                    if inventory["Health potion"] > 0: #if you have a health potion, it heals the player
                        print(f"Hp: {player_hp}") #prints hp prior to healing
                        print("Healing...") 
                        time.sleep(1)
                        inventory["Health potion"] -= 1 #subtracts one from the health potion inventory
                        player_hp += int(player_dragon['hp'] / 4) #heals the players hp by 1/4 of max 
                        if player_hp > player_dragon['hp']: #ensures hp doesnt go above max hp
                            player_hp = player_dragon['hp']
                        print("Healing comeplete!")
                        print(f"HP: {player_hp}. Healed by {int(player_dragon['hp'] / 4)}HP (Less if hp reached full.) ") #shows player how much the healed
                        print("-1 Health potion.")
                        print(f"{inventory["Health potion"]} Health potions remaining.") #prints remaining health potions
                    else:
                        print("No health potions available")
                    input("Press enter to continue: \n")
                            
                if choice == 3:
                    print("Exiting the battle...")
                    return # i didnt talk about return earlier, it exits the current funtion
                elif not choice == 1 and not choice == 2 and not choice == 3: #i probably could have just used else but im not changing it now
                    print("Invalid Move")
                    input("Press enter to continue: \n")
            except ValueError:
                print("invalid move")
                input("Press enter to continue: \n")

        if enemy_hp > 0: #as long as the enemy isn't defeated, it attacks
            print("Enemy turn!")
            time.sleep(1)
            print("enemy thinking..")
            time.sleep(1)
            enemy_damage = random.randint(int(wild_enemy["max_damage"] * 0.8), int(wild_enemy["max_damage"] + 1)) #same calculation as the players damage
            player_hp -= enemy_damage #damages player
            print(f"Enemy dealt {enemy_damage} damage, {player_hp} hp remaining") #prints damage dealt and remaining hp
            if player_hp < 0: #endsures player hp does not go below 0
                player_hp == 0
            turn = 1
        input("Press enter to continue: \n")
    if enemy_hp <= 0: #if enemy has no hp left, the player wins
        clear_screen()
        print("You win the battle! ")
        max_wild_level += 2
        max_player_level += 2
        print(f"Max level is now lvl{max_player_level} Which is +2 to previouse max level:{max_player_level - 2}")
        input("Press enter to catch:\n ")
        if inventory["Cow carcass"] > 0: #if player has a cow carcass to catch dragon, they are given the option to.
            catch() #runs function to catch the dragon
            return
        else:
            print("Sorry, no dragon for you.")
            print("You need a cow carcass to tame a dragon")
            print("Find one by exploring.")
    if player_hp <= 0: #if player dies:
        print("You lost the battle ):")
        print("returning to the main menu")
        return

def catch(): #catch funtion, only used when player wins a battle and has a cow carcass
    global inventory, dragons, wild_enemy #sets global variables
    clear_screen() 
    print(f"Name: {wild_enemy["name"]} | Level: {wild_enemy['level']} | HP: {wild_enemy['hp']} | Max Damage: {wild_enemy['max_damage']}") #reprints the enemy's stats
    print("Would you like to catch this dragon?")
    print("1: Yes")
    print("2: No")
    if input("Enter choice here:\n ") == "1": #if player chooses to catch the dragon:
        inventory["Cow carcass"] -= 1
        dragons.append(create_dragon(input("Enter a name for your dragon:\n "), wild_enemy["level"], input("Enter a name for your dragons move:\n "), wild_enemy["max_damage"])) # a more coplicated line, but it creates a dragon and allows player to input name and move name of new dragon
        print("Added to collection!")
    else:
        print("Ok, returning to main menu.")
        input("Press enter to continue:\n")
        return

def view_dragons(): #the view dragons function
    global dragons #sets global variable
    clear_screen()
    for i, dragon in enumerate (dragons, start=1): #another enumerate, this time printing all your dragons.
        print(f"{i}: Name: {dragon["name"]} | Level: {dragon["level"]} | Move: {dragon["move"]} | Max Damage: {dragon["max_damage"]}") #prints the dragons
    print("Would you like to use a training manual on a dragon?")
    print("1: Yes")
    print("2: No")
    if input("Enter choice here:\n ") == '1': #if player wants to use a training manual:
        clear_screen()
        print("In that case, which dragon would you like to use a training manual on?")
        for i, dragon in enumerate (dragons, start=1): #prints dragons again, just a copy of the one above
            print(f"{i}: Name: {dragon["name"]} | Level: {dragon["level"]} | HP: {dragon["hp"]} | Move: {dragon["move"]} | Max Damage: {dragon["max_damage"]}")
        try: #another try funtion, yet again
            print("(print an invalid input if you dont want to select a dragon)") 
            choice = (int(input("Enter choice here:\n ")) - 1) #sets choice to input,subtracting one like in the battle function
        except ValueError: 
            print("Please input a valid number")
            return
        
        if choice + 1 > len(dragons): #adds one because the list starts at zero, but if there is only one dragon with an index of 0, the length will still be 1.
            clear_screen()
            print("Invalid input")
            input("Press enter to return home: \n")
            return
        
        if inventory["Training manual"] > 0 and dragons[choice]['level'] < max_player_level: #if the player has a training manual and the dragon is not max level:
            dragons[choice]['level'] += 1 #increases level
            dragons[choice]['hp'] = int(dragons[choice]['level'] * 10) #increases hp so that it alligns with the new level
            dragons[choice]['max_damage'] = int(dragons[choice]['hp'] * 0.3) #increases max damage so that it alligns with the new hp
            inventory["Training manual"] -= 1 #gets rid of one training manual
            print(f"{inventory["Training manual"]} Training manuals remaining.") #prints remaining training manuals
            print("Training Manual used. Level, Hp and Damage increased.")
        elif inventory["Training manual"] < 1: #if player has no training manuals:
            clear_screen()
            print("You have no training manuals.")
            print("You need to find one by exploring.")
            input("Press enter to continue: \n")
            return
        elif dragons[choice]['level'] >= max_player_level: #if the dragon is already at max level:
            clear_screen()
            print("Your dragon is already max level.")
            print("You cannot use a training manual on it.")
            input("Press enter to continue: \n")
            return
        clear_screen()
        print("Your dragon has been trained!")

        print(f"You chose {dragons[choice]['name']}")
        print(f"Level: {dragons[choice]['level']} (+ 1)")
        print(f"Hp: {dragons[choice]['hp']} (+ 10)")
        print(f"Move: {dragons[choice]['move']}")
        print(f"Damage: {dragons[choice]['max_damage']} (+3)")
        #dumps a bunch of info about the dragon that was trained.
        input("\n Press enter to continue")
    else:
        clear_screen()
        print("Okay, returning home.")
        input("Press enter to continue: \n ")
    
# Main program starts here

clear_screen()

dragons = [
    {
        "name": str(input("Name your first dragon: \n")),
        "level": 6,
        "hp": 60,
        "move": "Fire breath",
        "max_damage": 18
    }
] #creates teh first dragon, which the player can train

while 0 == 0: #main gameloop, 0 always = 0, so it can only be exited by using break
    menu_choice = main_menu()

    if menu_choice == 1: 
        explore() #explore funtion is called
        input("Press enter to continue: \n ")
    elif menu_choice == 2:
        view_inventory() #view inventory function is called
    elif menu_choice == 3:
        view_dragons() #view dragons function is called
    elif menu_choice == 4:
        print("You will be missed ):")
        print("Thanks for playing dragon hunter")
        break #ends loop

    else:
        print("Real option please!") # if the user inputs an invalid option, it prints this message
        input("Press enter to continue: \n") #might not have mentioned this before, but it allows the player to take as long as they want to read the output before continuing.