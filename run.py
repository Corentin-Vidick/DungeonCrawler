"""
Import functions
"""
import random
import os

# Global variables
legend = {
    "dark": "  ",
    "empty": ". ",
    "player": "P ",
    "wall": "# ",
    "skel": "S ",
    "door": "E "
}


class Entity:
    """
    Creates an entity, player, enemy...
    """
    def __init__(self, pos, health, attack):
        self.pos = pos
        self.health = health
        self.attack = attack


player = Entity(0, 2, 1)
skeleton = Entity(random.randint(3, 23), 2, 1)
door = 24


rooms = []


class Room:
    """
    Creates an empty, dark room
    status matches legend options
    sontents to add future objects (sword, shield...)
    pos
    """
    def __init__(self, status, contents, pos):
        self.status = status
        self.contents = contents
        self.pos = pos


def clear_screen():
    """
    Clears terminal to improve UX
    """
    os.system("cls" if os.name == "nt" else "clear")


def menu():
    """
    Displays the start of game menu: play, rules and credits
    """
    clear_screen()
    print("Welcome to Coco's Dungeon Crawler\n\n")
    print("\n 1 - New game\n")
    print("\n 2 - Rules\n")
    print("\n 3 - Credits\n")
    while True:
        i = input("\n...")
        if i in ("1", "2", "3"):
            break
    if i == "1":
        clear_screen()
        print("Let's go!\n\n\n")
    elif i == "2":
        rules()
    elif i == "3":
        dev_credits()


def rules():
    """
    Displays the rules to the player
    """
    clear_screen()
    print("Hello adventurer, here is your challenge:\n\nYou will have to find \
your way through the dungeon and escape through the door.\n\nCareful though\
, skeletons are guarding the area.\n\nEach turn, you will choose a \
direction to go, your life depends on your choices!")
    print("\n\n\nEnter any key to go back to menu")
    while True:
        i = input()
        if i:
            break
    menu()


def dev_credits():
    """
    Displays the credits to the player
    """
    clear_screen()
    print("\n\n\nThis game is developed by Corentin Vidick\n\n\n")
    print("Enter any key to go back to menu")
    while True:
        i = input()
        if i:
            break
    menu()


def create_map():
    """
    Creates map array
    Initialise player position
    Initialise exit position
    """
    # Create empty map
    for i in range(25):
        room = Room("dark", "nothing", i)
        rooms.append(room)
    # Place player
    rooms[player.pos].status = "player"
    # Place exit door - remove after testing
    rooms[door].status = "door"
    # Place skeleton - remove after testing
    rooms[skeleton.pos].status = "skel"


def player_action_choice():
    """
    Asks for input for player action
    Rest, see map or move
    """
    choice = input("Would you like to rest ('1'), look at your map ('2')\
 or move('3')?\n...")
    if choice == "1":
        rest()
    elif choice == "2":
        show_map()
    elif choice == "3":
        player_movement_choice()
        check_movement_result()
    else:
        print("Wrong input, please try again\n")
        player_action_choice()


def rest():
    """
    Gives a small chance to the player to gain one life back
    """
    chance = random.randint(1, 10)
    if chance == 1:
        player.health += 1
        print("Your rest was fruitful, you have gained a life!")
    else:
        print("You had nightmares and woke up the same as before...")


def show_map():
    """
    Shows the map to the player and how many lives they have left
    """
    clear_screen()
    print("\nMap:\n")
    # one line the assignement and print?
    map_design = draw_map()
    print(map_design)
    # end of one line?
    life = player.health
    print(f"You have {life} health left\n")


def draw_map():
    """
    Creates the map to be viewed by player
    """
    map_string = ""
    pos = 0
    for i in range(5):
        for j in range(5):
            map_string += (legend[rooms[pos].status])
            pos += 1
        map_string += "\n"
    return map_string


def player_movement_choice():
    """
    Asks for input to move player
    Only gives possible options
    """
    print("\n...Checking possible movements...\n")
    for room in (rooms):
        if room.status == "player":
            move_up = False if room.pos in (0, 1, 2, 3, 4) else True
            move_down = False if room.pos in (20, 21, 22, 23, 24) else True
            move_left = False if room.pos in (0, 5, 10, 15, 20) else True
            move_right = False if room.pos in (4, 9, 14, 19, 24) else True
    print("Would you like to go:")
    if move_up:
        print("go up ('1')")
    if move_down:
        print("go down ('2')")
    if move_left:
        print("go left ('3')")
    if move_right:
        print("go right ('4')")
    direction = input("...")
    if direction not in ("1", "2", "3", "4"):
        print("\nWrong input, please try again\n")
        player_movement_choice()
    else:
        move_player(direction)


def move_player(direction):
    """
    Moves player if possible
    Otherwise returns to asking direction
    """
    # Needs some work on conditions for movement
    print("\n...Moving player...\n")
    if direction == "1" and player.pos > 4:
        rooms[player.pos].status = "empty"
        player.pos -= 5
        rooms[player.pos].status = "player"
    elif direction == "2" and player.pos < 20:
        rooms[player.pos].status = "empty"
        player.pos += 5
        rooms[player.pos].status = "player"
    elif direction == "3" and player.pos not in (0, 5, 10, 15, 20):
        rooms[player.pos].status = "empty"
        player.pos -= 1
        rooms[player.pos].status = "player"
    elif direction == "4" and player.pos not in (4, 9, 14, 19, 24):
        rooms[player.pos].status = "empty"
        player.pos += 1
        rooms[player.pos].status = "player"
    else:
        print("Impossible move, please try again\n")
        player_movement_choice()


def check_movement_result():
    """
    Checks what the player has encountered after their move
    """
    print("...Checking where you are...")
    if player.pos == door:
        victory()
    elif player.pos == skeleton.pos:
        encounter()
    else:
        no_event()


def no_event():
    """
    When player enters an empty room
    """
    clear_screen()
    print("\nYou enter the room slowly, trying to look in every direction \
at the same time...\nThe room is safe, but empty\n")


def encounter():
    """
    When player encounters a skeleton
    """
    clear_screen()
    fight_or_flight = input("\nYou have encountered a skeleton! Would you \
like to fight ('1') or retreat ('2')?\n...")
    if fight_or_flight == "1":
        fight()
    elif fight_or_flight == "2":
        flight()
    else:
        print("\nWrong input, please try again\n")
        encounter()


def fight():
    """
    Fight against a skeleton
    """
    print("\nYou fight the skeleton...\n")
    while player.health != 0 and skeleton.health != 0:
        i = random.randint(1, 10)
        if i == 1:
            print("\nBoth miss!")
        elif i in (2, 3):
            print("\nThe skeleton lands a blow!")
            player.health -= skeleton.attack
        elif i == 4:
            print("\nYou both hit each other at the same time!")
            player.health -= skeleton.attack
            skeleton.health -= player.attack
        elif i == 5:
            print("\nYou manage to deal a critical hit!")
            skeleton.health -= player.attack + 1
        else:
            print("\nYou hit the skeleton!")
            skeleton.health -= player.attack
    if player.health == 0:
        defeat()
    elif skeleton.health == 0:
        print("\nYou defeated the skeleton! A pile of bones now lays at your \
feet\n")
        rooms[skeleton.pos].status = "player"


def flight():
    """
    Flee from a skeleton
    """
    direction = random.randint(1, 2)
    if direction == 1:
        print("\nYou failed to escape, you have to fight")
        fight()
    elif direction == 2:
        print("\nYou run away blindly...\n")
        i = str(random.randint(1, 4))
        move_player(i)


def victory():
    """
    When player reaches the exit
    Resets player position and life
    """
    clear_screen()
    print("\n\nYou made it out!\n!!!Congratulations!!!\n\n")
    player.health = 0


def defeat():
    """
    When player runs out of lives
    Resets player position
    """
    clear_screen()
    print("\n\nYou died!\n!!!Better luck next time!!!\n\n")


if __name__ == "__main__":
    print("Starting game...\n")
    menu()
    create_map()
    while player.health:
        player_action_choice()
    # map = []
    player = Entity(0, 2, 1)
    skeleton = Entity(random.randint(3, 23), 1, 1)
    door = Entity(24, None, None)
