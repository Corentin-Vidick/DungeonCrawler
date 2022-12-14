"""
Import functions
"""
import random
import os

# Lines of code from
# https://www.youtube.com/watch?v=u51Zjlnui4Y&ab_channel=TechWithTim
# - START -
import colorama
from colorama import Fore, Back, init
init(autoreset=True)
# - END -

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
    print(f"{Fore.BLUE}Welcome to Coco's Dungeon Crawler\n\n")
    print(f"\n {Back.MAGENTA}1{Back.RESET} - New game\n")
    print(f"\n {Back.MAGENTA}2{Back.RESET} - Rules\n")
    print(f"\n {Back.MAGENTA}3{Back.RESET} - Credits\n")
    while True:
        i = input("\n...\n")
        if i in ("1", "2", "3"):
            break
        print(
            f"{Fore.GREEN}{i} is not an option, "
            "let's be nice and follow the guide\n")
    if i == "1":
        # Allows Colorama to reset colors to default
        print("")
        clear_screen()
        print(f"{Fore.BLUE}Let's go!\n\n\n")
    elif i == "2":
        rules()
    elif i == "3":
        dev_credits()


def rules():
    """
    Displays the rules to the player
    """
    # Allows Colorama to reset colors to default
    print("")
    clear_screen()
    print(
        "\n\n\nHello adventurer, here is your challenge:\n\n"
        "You will have to make your way through the dungeon and "
        "find the secret "
        f"{Fore.YELLOW}exit"
        f"{Fore.WHITE}.\n\nCareful though, "
        f"{Fore.RED}skeletons "
        f"{Fore.WHITE}are guarding the area.\n\n"
        "You can rest to gain "
        f"{Fore.GREEN}health\n\n"
        f"{Fore.WHITE}Each turn, you will choose a direction to go, "
        "your life depends on your choices!\n\n\n"
    )
    print(f"{Back.MAGENTA}\n\n\nPress Enter key to go back to menu")
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
    # Allows Colorama to reset colors to default
    print("")
    clear_screen()
    print(
        "\n\n\nThis game is developed by Corentin Vidick\n\n\n"
        "For the best experience play on Google Chrome browser. "
        "Playing on another browser might cause issues "
        "with the display of emoticons."
    )
    print(f"{Back.MAGENTA}\n\n\nPress Enter key to go back to menu")
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
            f"Would you like to rest {Back.MAGENTA}1"
            f"{Back.RESET}, look at your map {Back.MAGENTA}2"
            f"{Back.RESET} or move {Back.MAGENTA}3"
            f"{Back.RESET}?\n...\n"
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
    # else:
    #    print("Wrong input, please try again\n")
    #    player_action_choice()


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
    print(
        f"\nYou have "
        f"{Fore.GREEN}{life} health "
        f"{Fore.WHITE}left\n"
    )


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
    print(f"{Fore.CYAN}\n...Checking possible movements...\n")
    options = check_possible_moves()
    print("Would you like to:")
    if moves["up"]:
        print(f"go up {Back.MAGENTA}1")
    if moves["down"]:
        print(f"go down {Back.MAGENTA}2")
    if moves["left"]:
        print(f"go left {Back.MAGENTA}3")
    if moves["right"]:
        print(f"go right {Back.MAGENTA}4")
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
    print(f"{Fore.CYAN}\n...Moving player...\n")
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
    print(f"{Fore.CYAN}...Checking where you are...")
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
            f"\nYou have encountered a {Fore.RED}skeleton"
            f"{Fore.WHITE}! Would you like to fight {Back.MAGENTA}1"
            f"{Back.RESET} or retreat {Back.MAGENTA}2{Back.RESET}?\n...\n"
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
            print(f"{Fore.RED}\nThe skeleton lands a blow!")
            player.health -= skeleton.attack
        elif i == 4:
            print("\nYou both hit each other at the same time!")
            player.health -= skeleton.attack
            skeleton.health -= player.attack
        elif i == 5:
            print(f"{Fore.CYAN}\nYou manage to deal a critical hit!")
            skeleton.health -= player.attack + 1
        else:
            print(f"{Fore.CYAN}\nYou hit the skeleton!")
            skeleton.health -= player.attack
    if player.health == 0:
        defeat()
    elif skeleton.health == 0:
        print(
            f"{Fore.GREEN}\nYou defeated the skeleton! A pile of bones now "
            "lays at your feet\n"
        )
        rooms[skeleton.pos].status = "player"


def flight():
    """
    Flee from a skeleton
    """
    escape = random.randint(1, 2)
    if escape == 1:
        print(f"{Fore.RED}\nYou failed to escape, you have to fight")
        fight()
    elif escape == 2:
        print(f"{Fore.BLUE}\nYou run away blindly...\n")
        i = check_possible_moves()
        move_player(random.choice(i))


def victory():
    """
    When player reaches the exit
    Resets player position and life
    """
    clear_screen()
    print(f"{Fore.GREEN}\n\nYou made it out!\n!!!Congratulations!!!\n\n")
    player.health = 0


def defeat():
    """
    When player runs out of lives
    Resets player position
    """
    rooms[player.pos].status = "dead"
    show_map()
    print(f"{Fore.RED}\n\nYou died!\n!!!Better luck next time!!!\n\n")


def run_game():
    """
    Game run function
    """
    print(f"{Fore.CYAN}Starting game...\n")
    menu()
    create_map()
    while player.health:
        player_action_choice()


if __name__ == "__main__":
    while True:
        run_game()
        while True:
            i = input(
                "\nYou have reached the end of the game! Would "
                f"you like to restart {Back.MAGENTA}1"
                f"{Back.RESET} or leave {Back.MAGENTA}2"
                f"{Back.RESET}?\n...\n"
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
