"""
Import functions
"""
import random
import os

# Global variables
legend = {
    "dark": "  ",
    "empty": "👣 ",
    "player": "🧍 ",
    "wall": "🧱 ",
    "skeleton": "💀 ",
    "dead": "⚰️ ",
    # TODO: remove door legend after testing
    # "door": "🚪 "
}


moves = {
    "up": False,
    "down": False,
    "left": False,
    "right": False
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
door = random.randint(3, 23)
while skeleton.pos == door:
    door = random.randint(3, 23)


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
        i = input("\n...\n")
        if i in ("1", "2", "3"):
            break
        print(f"{i} is not an option, let's be nice and follow the guide\n")
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
    print(
        "\n\n\nHello adventurer, here is your challenge:\n\n"
        "You will have to find your way through the dungeon and escape "
        "through the door.\n\nCareful though, skeletons are guarding the "
        "area.\n\nYou can rest to gain health.\n\n"
        "Each turn, you will choose a direction to go, "
        "your life depends on your choices!\n\n\n"
    )
    print("\n\n\nPress Enter key to go back to menu")
    while True:
        i = input("\n")
        if i == "":
            break
        print(f"{i} is wrong, please press Enter key...")
    menu()


def dev_credits():
    """
    Displays the credits to the player
    """
    clear_screen()
    print(
        "\n\n\nThis game is developed by Corentin Vidick\n\n\n"
        "For the best experience play on Google Chrome browser. "
        "Playing on another browser might cause issues "
        "with the display of emoticons."
    )
    print("\n\n\nPress Enter key to go back to menu")
    while True:
        i = input("\n")
        if i == "":
            break
        print(f"{i} is wrong, please press Enter key...")
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
    # TODO: Place exit door - remove after testing
    # rooms[door].status = "door"
    # TODO: Place skeleton - remove after testing
    # rooms[skeleton.pos].status = "skeleton"


def player_action_choice():
    """
    Asks for input for player action
    Rest, see map or move
    """
    while True:
        choice = input(
            "Would you like to rest ('1'), "
            "look at your map ('2') "
            "or move('3')?\n...\n"
        )
        if choice in ("1", "2", "3"):
            break
        print(f"{choice} is wrong, please try again...")
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
    print(draw_map())
    life = player.health
    print(f"\nYou have {life} health left\n")


def draw_map():
    """
    Creates the map to be viewed by player
    """
    map_string = ""
    pos = 0
    map_string += legend["wall"] * 7
    map_string += "\n"
    for i in range(5):
        map_string += legend["wall"]
        for j in range(5):
            map_string += (legend[rooms[pos].status])
            pos += 1
        map_string += legend["wall"]
        map_string += "\n"
    map_string += legend["wall"] * 7
    return map_string


def check_possible_moves():
    """
    Checks which directions the player can move in
    """
    options = []
    if player.pos in (0, 1, 2, 3, 4):
        moves["up"] = False
    else:
        moves["up"] = True
        options.append("1")
    if player.pos in (20, 21, 22, 23, 24):
        moves["down"] = False
    else:
        moves["down"] = True
        options.append("2")
    if player.pos in (0, 5, 10, 15, 20):
        moves["left"] = False
    else:
        moves["left"] = True
        options.append("3")
    if player.pos in (4, 9, 14, 19, 24):
        moves["right"] = False
    else:
        moves["right"] = True
        options.append("4")
    return options


def player_movement_choice():
    """
    Asks for input to move player
    Only gives possible options
    """
    print("\n...Checking possible movements...\n")
    options = check_possible_moves()
    print("Would you like to:")
    if moves["up"]:
        print("go up ('1')")
    if moves["down"]:
        print("go down ('2')")
    if moves["left"]:
        print("go left ('3')")
    if moves["right"]:
        print("go right ('4')")
    while True:
        direction = input("...\n")
        if direction in (options):
            break
        print(f"{direction} is wrong, please choose a valid option...")
    move_player(direction)


def move_player(direction):
    """
    Moves player if possible
    Otherwise returns to asking direction
    """
    print("\n...Moving player...\n")
    if player.pos == skeleton.pos and skeleton.health != 0:
        rooms[player.pos].status = "skeleton"
    else:
        rooms[player.pos].status = "empty"
    if direction == "1":
        player.pos -= 5
    elif direction == "2":
        player.pos += 5
    elif direction == "3":
        player.pos -= 1
    elif direction == "4":
        player.pos += 1
    rooms[player.pos].status = "player"


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
    print(
        "\nYou enter the room slowly, trying to look in every direction "
        "at the same time...\nThe room is safe, but empty\n"
    )


def encounter():
    """
    When player encounters a skeleton
    """
    clear_screen()
    while True:
        fight_or_flight = input(
            "\nYou have encountered a skeleton! Would you "
            "like to fight ('1') or retreat ('2')?\n...\n"
        )
        if fight_or_flight in ("1", "2"):
            break
        print(f"{fight_or_flight} is wrong, the skeleton is approaching...")
    if fight_or_flight == "1":
        fight()
    elif fight_or_flight == "2":
        flight()


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
        print(
            "\nYou defeated the skeleton! A pile of bones now lays at your "
            "feet\n"
        )
        rooms[skeleton.pos].status = "player"


def flight():
    """
    Flee from a skeleton
    """
    escape = random.randint(1, 2)
    if escape == 1:
        print("\nYou failed to escape, you have to fight")
        fight()
    elif escape == 2:
        print("\nYou run away blindly...\n")
        i = check_possible_moves()
        move_player(random.choice(i))


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
    rooms[player.pos].status = "dead"
    show_map()
    print("\n\nYou died!\n!!!Better luck next time!!!\n\n")


def run_game():
    """
    Game run function
    """
    print("Starting game...\n")
    menu()
    create_map()
    while player.health:
        player_action_choice()


if __name__ == "__main__":
    while True:
        run_game()
        while True:
            i = input(
                "\nYou have reached the end of the game! Would you "
                "like to restart ('1') or leave ('2')?\n...\n"
            )
            if i in ("1", "2"):
                break
            print(f"{i} is wrong, please choose a valid option...")
        if i == "2":
            break
        # Reset all entities for next game
        rooms = []
        player.pos = 0
        player.health = 2
        skeleton.pos = random.randint(1, 23)
        skeleton.health = 2
        door = random.randint(3, 23)
        while skeleton.pos == door:
            door = random.randint(3, 23)
