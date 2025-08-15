
# data.py
from config import *
player = {
    "location": "Start"
}
weapon_stats={}
player_stats={}

defences = []
weapons = []
abilities = []
items = []

current_defences = defences

Elissus_Rooms = {
    "your_room": {
        "choice": "To your left is a small wardrobe. In front of you, the door. (Avaliable commands: 'up', 'left')",
        "description": (
            "Starting the game... "
            "You wince as light comes through the window into your tiny room. "
            "Suddenly, you remember what day it is. You jump out of bed and get dressed. "
            "For going up, press w. For left, press a. For right, press d. For down, press s."
        ),
    },
    "your_wardrobe": {
        "choice": "To your left is the door leading outside. (Avaliable commands: 'up'.)",
        "description": "You investigate your worn wardrobe. Inside is 5 Elissian Coins! You take them."
    },
    "town_street": {
        "choice": "Right leads down the street. Left leads to Harraxx. (Avaliable commands: 'right', 'left')",
        "description": "You head outside into the bustling streets of Varrus. Kids are playing, adults are chatting, and Harraxx, your best friend, is calling to you."
    },
    "harraxx_house": {
        "choice": "You can go back to the street. (Avaliable commands: 'down')",
        "description": "You walk up to Harraxx. He's holding some money in his hand. He says, 'Since the Alignment is today, I thought you could have this spare money I found.' You got 10 Elissian Coins!"
    },
    "market_square": {
        "description": "You walk down the street, smiling at the peaceful atmosphere. A call from Elder Aksovv alerts you.",
        "choice": "Elder Aksovv is standing to the right. To the left, two kids. The portal is visible further up. (Avaliable commands: 'right', 'left', 'up')"
    },
    "elder_house": {
        "description": "Elder Aksovv greets you warmly. 'The Alignment is today, young one. Be ready.' He hands you a bouquet of flowers for the ceremony. You got the Festival Bouquet!",
        "choice": "You can go back to the market square. (Avaliable commands: 'down')",
        "items": ["festival_bouquet"]
    },
    "playing_area": {
        "description": "A group of kids are playing a game. They wave at you. 'Hey sir!' they say enthusiastically. 'I'm so excited for the Alignment! We can finally go explore the other planets!'",
        "choice": "You can go back to the market square. (Avaliable commands: 'down')"
    },
    "portal_gate": {
        "description": "People gather around as the portal hums wit energy. It's almost time.",
        "choice": "You can only go up. Press 'w' to continue.",
    },
    "elissus_portal": {
        "description": (
            "The portal to Elissus glows with energy. You can feel the pull of the Alignment. "
            "'For millennia, we have waited for this moment,' says Aksovv. 'Let us begin the ceremony.' "
            "Aksovv and the Second Elder hold hands and begin chanting in an ancient language. Slowly, the portal begins to creak open. Red sparks fly out, and the air hums with energy. "
            "Suddenly, the elders stop. 'What...is that?' Aksovv says, peering in. As he says that, the village simultaneously turn to see a crimson hand reaching out of the portal... ... "
            "It grabs Aksovv and pulls him in. The village erupts into chaos as blood-red entities pour out of the portal. You turn around, but a winged demon knocks you and you fall into the depths below..."
        ),
        "choice": "",
    },
    "sewer_depths": {
        "description": "Rubbing your head, you dizzily stand up to find yourself in a dark, damp sewer. On the floor is a small, blunt knife.",
        "choice": "The only way is forward. (Avaliable commands: 'up')",
        "items": ["blunt_knife"],
        "knife_yes": "Yes",
    },
    "sewer_end": {
        "description": "A cough comes from the end of the sewers. Running up, you find the Second Elder, suit stained in blood. Wheezing, he gasps 'Take it. Take my power. Save...them...' And he's gone.",
        "choice": "Continue ahead? (Avaliable commands: 'w')",
        "abilities": ["Growth"]
    },
    "Crimson_streets": {
        "save_point": "The game has been saved. To check your inventory, type 'i'. Otherwise, type anything else to continue.",
        "description": "The place you once knew as home is now an apocalyptic nightmare. A deep red has seemed to have taken over. Screams echo ahead of you.",
        "choice": "To head to the place of the screams, type 'w'. To head into the watchtower, type 'a'. To investigate a den near you, type 'd'."
    },
    "broken_portal": {
        "description": "A gate blocks the way forward. It seems that a switch must be deactivated to proceed.",
        "choice": "You must now head back. Press 'Enter' to continue.",
        "description1": "With the gate open you can now proceed into the clearing. There, a very familiar figure is waiting.",
    },
    "rat_den": {
        "description": "In a dark den below, two rats turn around and scream at you.",
        "choice": "Press 'Enter' to head back to the streets.",
        "items": ["Blessed Carrot"]
    },
    "elissus_tower": {
        "description": "A great tower ascends above you. The stairway wraps around the central spire.",
        "choice": "To further ascend, type 'w'. To head into a small room to the left, type 'a'.",
        "description1": "At the top, a statue glows with life and raises it's sword.",
        "choice1": "To continue to the top, type 'w'. To go back to the streets, type 's'.",
        "description2": "In the room, a tablet with a riddle lies.",
        "choice2": "To head back, type 's'.",
        "defence": ["Farmer Tunic"],
    },
    "elissus_puzzle_room": {
        "description": "You enter a small room with a glowing puzzle tablet.",
        "choice": "To return to the tower, type 's'."
    },
    "towertop": {
        "description": "A puzzle scroll sits in the room.",
        "choice": "To return, type 's'.",
    },
    "Torn Landing Pad": {
        "description": "The new lands are filled with white particles all around. A huge purple crack tears through the landing pad.",
        "description1": "In the white room, a chest glows with power. Inside is a new ability, Reality Shift!",
        "choice": "To the north is a gateway leading to a pale white room. Next to the doors is a strange-looking barrel. Avaliable commands: 'w' and 'a'.",
        "abilities": ["Reality Shift"]
    },
    "Elevator": {
        "description": "Stepping into the elevator, a loud cha-chunk resonates. As you head down, a scream echoes. A corpse falls into the elevator and opens its eyes.",
        "description1": "After giving the enemies the money, the elevator continues down into a new land...",
        "choice": "The elevator suddenly stops. A remote control sits at the end of the elevator. To the north, the room opens up to a great chasm. To the south, a darker part of the room. Avaliable commands: 'w' and 's'.",
        "choice1": "Press 'Enter' to continue",
        "items": ["Remote Control"],
    },
    "Southern Camp": {
        "description": "A soldier sits, back turned, facing the campfire.",
        "description1": "After defeating the soldier, you investigate the campsite to find an Ashen Pot in the chest.",
        "description2": "Past the campfire, three weapons lie connected by blue chains.",
        "choice": "You may either sneak past the soldier or engage. To sneak past, type 'w'. To engage, type 'd'.",
        "choice1": "You may only choose one weapon. 1 - Splitting Spear. 2 - Torn Flail. 3 - Hammer of the Fallen Hero.",
        "choice2": "After choosing a weapon, the rest disappear. Press 'w' to continue ahead.",
        "items": ["Ashen Pot"],
        "weapons": ["Splitting Spear", "Torn Flail", "Hammer of the Fallen Hero"]
    },
    "The Maw": {
        "description": "The world opens up to a red sky. Fields stretch out as winged demon-like birds fly around. As you try to advance, two Winged Crimsons land and attack.",
        "choice": "To continue ahead to the building, type 'w'. To go to the river nearby, type 'a'. To return to the camp, type 's'.",
    },
    "River East": {
        "description": "A ferryman with a small boat rests besides the river. They say 'To cross to the green lands, you must pay me 50 of your money.'",
        "description1": "On the other side, you continue on your way.",
        "choice": "To pay and cross, type 'w'. To return back, type 's'."
    },
    "Elevator Depths": {
        "description": "The lift comes to a clank as it reaches the bottom. A strange indigo energy resonates behind the elevator.",
        "choice": "To investigate the energy, type 's'. To continue, type 'w'.",
        "items": ["Darker Orb"]
    },
    "Majestical Clearing": {
        "description": "The light completely fills your eyes. Ahead is a beautiful clearing, the only place in this world where grass still grows.",
        "choice": "To talk to a strange person, type 'e'. To investigate a grove of herbs, type 'a'. To go over to the river type 'd'. To continue, type 'w'.",
        "description1": "The person is pale in the face. They need some sort of medicine.",
        "description2": "Light returns to the person's face. They stand up. 'Thank you. For saving me, i'll help you by giving better items through your mission.",
        "description3": "You head over to the field and pick 4 Fresh Medicinals.",
        "items": ["Medicinal Herb", "Medicinal Herb", "Medicinal Herb", "Medicinal Herb"]
    },
    "River West": {
        "description": "A ferryman with a small boat rests besides the river. They offer you free travel onto the ship to the other side.",
        "description1": "Once you're on the other side, you continue along to the haven.",
        "choice": "To board the ferry, type 'w'. To return to the haven, type 's'."
    },
    "Lower Labs": {
        "description": "You enter the white building. A scientist with bright yellow eyes looks at you frantically and pulls out a knife.",
        "description1": "After the battle, a puzzle stands in your way.",
        "choice": "Press 'Enter' to continue.",
        "items": ["Strange Brew"],
    },
    "Singularity Lab": {
        "description": "On the inside, multiple tubes connect to a humanoid in the centre tube. Suddenly, the glass cracks and the scientist seeps out."
    },
}

enemy_stats = {
    "enemy_data": {
        "Crimson Rat": {
            "health": [15, 20, 20, 20, 25],
            "damage": [5, 5, 5, 5, 10],
            "drops": ["", "", "", "", "Rat Tail"],
        },
        "Crimson Rats": {
            "health": [30, 40, 40, 40, 50],
            "damage": [5, 10, 10, 12, 15, 15],
            "drops": ["","","","Rat Tail", "Rat Tail"],
        },
        "Living Statue": {
            "health": [20, 20, 25, 25, 25],
            "damage": [5, 6, 8, 10, 10, 10],
            "drops": [""]
        },
        "Fragmented Husk": {
            "health": [30, 30, 30, 30, 40],
            "damage": [5, 5, 5, 15, 20],
            "drops": [""]
        },
        "Mysterious Soldier": {
            "health": [40, 45, 45],
            "damage": [10, 10, 10, 20, 20],
            "drops": [""]
        },
        "Winged Crimsons": {
            "health": [40, 50, 50, 50, 55],
            "damage": [15, 18, 25],
            "drops": ["", "", "", "Old Wing", "Old Wing"]
        },
        "Mad Scientist": {
            "health": [50, 60, 60, 60],
            "damage": [20, 20, 20, 25, 25, 25, 25, 30, 30, 30, 35, 35, 40],
            "drops": [""]
        }
    },
}

boss_stats = {
    "Harraxx, Elissian Zero": {
        "health": 50,
        "attacks1": {
            "Roar": {
                "damage": [5, 5, 5, 5, 15],
            },
            "Claw Swipe": {
                "damage": [5, 10, 10, 10, 20],
            },
        },
        "attacks2": {
            "Roar": { 
                "damage": [5, 5, 5, 5, 15],
            },
            "Claw Swipe": {
                "damage": [5, 10, 10, 10, 20],
            },
            "Stomp": {
                "damage": [6, 6, 6, 6, 6, 30]
            },
        },
        "attacks3": {
            "Roar": { 
                "damage": [3, 3, 3, 3, 13],
            },
            "Claw Swipe": {
                "damage": [3, 8, 8, 8, 18],
            },
            "Stomp": {
                "damage": [4, 4, 4, 4, 4, 28]
            },
        },
        "attacks4": {
            "Roar": { 
                "damage": [0, 0, 0, 0, 10],
            },
            "Claw Swipe": {
                "damage": [0, 5, 5, 5, 15],
            },
            "Stomp": {
                "damage": [1, 1, 1, 1, 1, 1, 25]
            },
        },
        "attacks5": {
            "Roar": { 
                "damage": [10, 10, 10, 10, 30],
            },
            "Claw Swipe": {
                "damage": [10, 20, 20, 20, 40],
            },
            "Stomp": {
                "damage": [12, 12, 12, 12, 12, 12, 60]
            },
        },
        "attacks6": {
            "Roar": {
                "damage": [2, 2, 2, 2, 8],
            }
        },
        "dialogue": {
            "1": "The figure stands confidently.",
            "2": "Goo drips off the body.",
            "3": "A slight wheezing escapes their mouth",
            "4": "The back hunches over.",
            "5": "A mighty roar unleashes.",
            "6": "It collapses to the floor",
            "7": "The lights in its eyes slowly fade...",
        },
    },
}

ability_stats = {
    "Growth": {
        "description": "A vine wrapped around your right arm. When you call it at the right moment, you may be able to save someone you love."
    },
    "Reality Shift": {
        "description": "Violet energy pulsating from your chest with a faint glow. For every shift between light and dark, your physical power decreases."
    }
}

item_stats = {
    "Festival Bouquet": {
        "description": "Given by the First Elder. It's scent remains fresh even in the ashen world. Some creatures may be drawn to it."
    },
    "Blessed Carrot": {
        "description": "The only surviving piece of the once-fertile land. Emits a yellow glow."
    },
    "Rat Tail": {
        "description": "A cut off part of a rat's tail. It bubbles and oozes even after its seperation."
    },
    "Old Wing": {
        "description": "A wing deteriorated from the corrupted flyers."
    },
    "Remote Control": {
        "description": "In the last Alignment, Nolox gave many of these to Fragira. This is one of the last."
    },
    "Ashen Pot": {
        "description":  "Inside the pot is dust. Who's dust? Impossible to tell..."
    },
    "Darker Orb": {
        "description": "Imagine the darkest shade of black possible. This is darker."
    },
    "Fresh Medicinal": {
        "description": "The lowest level of healing in the lands, but still useful."
    },
    "Strange Brew": {
        "description": "No one knows what's in this. Apparently it's some kind of poison. Just try it to find out."
    }
}

weapon_stats = {
    'Blunt Knife': {
        "description": "It's as if someone banged this on a rock. Except that it looks worse than that.",
        "damage": [8, 8, 8, 8, 16]
    },
    'Splitting Spear': {
        "description": "If it lands in the right place, it'll do serious damage. That's a big if though.",
        "damage": [12, 12, 12, 12, 12, 60]
    },
    'Torn Flail': {
        "description": "The very flail has a hole though it, but that doesn't stop it from dealing good damage.",
        "damage": [20, 25]
    },
    'Hammer of a Fallen Hero': {
        "description": "Once the hero wielded it. But they don't anymore, so the power has decreased.",
        "damage": [5, 10, 10, 15, 15, 15, 20, 20, 20, 20, 25, 25, 25, 30, 30, 40]
    }
}

defence_stats = {
    'Farmer Tunic': {
        "description": "A worn, old tunic offering little protection. But a little is better than none.",
        "defence": 5
    }
}
if current_defences:
    defence = (defence_stats[current_defences[0]]["defence"])
else:
    defence = 1

game_state = {
    "p_health": p_health,
    "p_max_health": p_max_health,
    "p_name": p_name,
    "p_progress": p_progress,
    "p_damage": p_damage,
    "p_defence": p_defence,
    "p_currency": p_currency,
    "p_location": p_location,
    "enemy": enemy,
    "enemy_name": enemy_name,
    "enemy_drops": enemy_drops,
    "enemy_damage_amount": enemy_damage_amount,
    "player_damage_amount": player_damage_amount
}