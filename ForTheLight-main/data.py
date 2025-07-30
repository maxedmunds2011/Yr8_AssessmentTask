# data.py
print("Loading data.py")
print("Loading functions.py")

import shared

rooms = {
    "cell": {
        "description": "A cold detention cell with dim lights and a locked door to the north.",
        "exits": {"north": "hallway"},
        "items": []
    },
    "hallway": {
        "description": "A narrow hallway patrolled by droids. East leads to a control room. West leads to an armoury.",
        "exits": {"south": "cell", "east": "control_room", "west": "armoury"},
        "items": []
    },
    "armoury": {
        "description": "Stacks of weapons and equipment. There’s a blaster on the shelf.",
        "exits": {"east": "hallway"},
        "items": ["blaster"]
    },
    "control_room": {
        "description": "Screens flash with security alerts. A terminal glows. North leads to the escape pod.",
        "exits": {"west": "hallway", "north": "escape_pod"},
        "items": ["keycard"]
    },
    "escape_pod": {
        "description": "A single escape pod sits waiting. The panel blinks: Insert Keycard.",
        "exits": {"south": "control_room"},
        "items": []
    },

    # New rooms start here
    "barracks": {
        "description": "Bunks, lockers, and signs of a recent fight. Blood on the wall.",
        "exits": {"south": "armoury"},
        "items": ["medkit"]
    },
    "ventilation": {
        "description": "A narrow, dark vent. You can hear voices above. There's a grate leading east.",
        "exits": {"east": "server_room", "west": "control_room"},
        "items": []
    },
    "server_room": {
        "description": "Banks of computers and humming lights. An access chip lies on the floor.",
        "exits": {"west": "ventilation"},
        "items": ["access_chip"]
    },
    "hangar": {
        "description": "A giant hangar bay with TIE fighters. A door to the north reads 'EXIT'.",
        "exits": {"north": "freedom_gate", "south": "escape_pod"},
        "items": []
    },
    "freedom_gate": {
        "description": "Security gate with retina scanner. Requires access chip to pass.",
        "exits": {},
        "items": []
    }
}


Elissus_Rooms = {
    "your_room": {
        "choice": "To your left is a small wardrobe. In front of you, the door. (Avaliable commands: 'up', 'left')",
        "description": 
            "Starting the game... "
            "You wince as light comes through the window into your tiny room. "
            "Suddenly, you remember what day it is. You jump out of bed and get dressed. "
            "For going up, press w. For left, press a. For right, press d. For down, press s. "
        ,
    },
    "your_wardrobe": {
        "choice:": "To your left is the door leading outside. (Avaliable commands: 'up'.)",
        "description": {
            "You investigate your worn wardrobe. Inside is 5 Elissian Coins! You take them."
        }
    },
    "town_street": {
        "choice": "Right leads down the street. Left leads to Harraxx. (Avaliable commands: 'right', 'left')",
        "description": {
            "You head outside into the bustling streets of Varrus."
            "Kids are playing, adults are chatting, and Harraxx, your best friend, is calling to you."
        }      
    },
    "harraxx_house": {
        "choice": "You can go back to the street. (Avaliable commands: 'down')",
        "description": { 
            "You walk up to Harraxx. He's holding some money in his hand."
            "He says, 'Since the Alignment is today, I thought you could have this spare money I found.'"
            "You got 10 Elissian Coins!"
        }
    },
    "market_square": {
        "description": "You walk down the street, smiling at the peaceful atmosphere. A call from Eldor Aksovv alerts you.",
        "choice": {
            "Elder Aksovv is standing to the right. To the left, two kids. The portal is visible further up. (Avaliable commands: 'right', 'left', 'up')"
        }
    },
    "elder_house": {
        "description": {
            "Elder Aksovv greets you warmly. 'The Alignment is today, young one. Be ready. '"
            "He hands you a bouquet of flowers for the ceremony."
            "You got the Festival Bouquet!"
        },
        "choice": "You can go back to the market square. (Avaliable commands: 'down')",
        "items": ["festival_bouquet"]
    },
    "playing_area": {
        "description": {
            "A group of kids are playing a game. They wave at you.",
            "'Hey sir!' they say enthusiastically. 'I'm so excited for the Alignment! We can finally go explore the other planets!'"        
        },
        "choice": "You can go back to the market square. (Avaliable commands: 'down')"
    },
    "portal_gate": {
        "description": "A shimmering portal stands before you, ready for the Alignment. The Second Elder is waiting.",
        "choice": "You can go back to the market square or continue for the Opening Ceremony. (Avaliable commands: 'down', 'up')"
    },
    "elissus_portal": {
        "description": {
            "The portal to Elissus glows with energy. You can feel the pull of the Alignment."
            "'For millennia, we have waited for this moment,' says Aksovv. 'Let us begin the ceremony.'"
            "Aksovv and the Second Elder hold hands and begin chanting in an ancient language."
            "Slowly, the portal begins to creack open. Red sparks fly out, and the air hums with energy."
            "Suddenly, the elders stop. 'What...is that?' Aksovv says, peering in."
            "As he says that, the village simultaneously turn to see a crimson hand reaching out of the portal..."
            "..."
            "It grabs Aksovv and pulls him in. The village erupts into chaos as blood-red entities pour out of the portal."
            "You turn around, but a winged demon knocks you and you fall into the depths below..."
        },
        "choice": {}, 
    },
    "sewer_depths": {
        "description": {
            "Rubbing your head, you dizzily stand up to find yourself in a dark, damp sewer."
            "On the floor is a small, blunt knife."
            "Suddenly, something in the pale green water catches your eye."
            "A rat, with glowing red eyes, is staring at you."
            "Grabbing the knife, you prepare for a fight."
        },
        "choice": "The only way is forward. (Avaliable commands: 'up')",
        "items": ["blunt_knife"],
        "enemy": 
        {
            "name": "Crimson Rat",
            "health": [20, 25, 25, 25, 30],
            "damage": [5, 5, 5, 5, 10]
        }
    },
}

enemy_stats = {
    "enemy_data": {
        "Crimson Rat": {
            "health": [15, 20, 20, 20, 25],
            "damage": [5, 5, 5, 5, 10],
            "drops": ["","","","","Rat Tail"]
        },
    },
}