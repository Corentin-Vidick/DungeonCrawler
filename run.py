"""
Import random function
"""
import random

# Global variables
player = {
    "room": 1,
    "life": 2
}

door = {
    "room": 24
}

skel = {
    "room": random.randint(3, 23)
}

legend = {
    "dark": "  ",
    "empty": ". ",
    "player": "P ",
    "wall": "# ",
    "skel": "S ",
    "door": "E "
}

rooms = []


class Room:
    """
    Creates an empty, dark room
    """
    def __init__(self, status, contents, row, column):
        self.status = status
        self.contents = contents
        self.row = row
        self.column = column


def print_positions():
    """
    Temporary function to print player's position
    """
    print(f"Player:{player}")
    print(f"Skeleton:{skel}")


def create_map():
    """
    Creates map array
    Initialise player position
    Initialise exit position
    """
    # Create empty map
    for x in range(5):
        for y in range(5):
            room = Room("empty", "nothing", x, y)
            rooms.append(room)
    # Place player
    rooms[1].status = "player"
    # Place exit door
    rooms[24].status = "door"
    # Place skeleton
    rooms[skel["room"]].status = "skel"


def player_action_choice():
    """
    Asks for input for player action
    Rest, see map or move
    """
    choice = input("Would you like to rest ('1'), look at your map ('2')\
 or move('3')?")
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
        player["life"] += 1
        print("Your rest was fruitful, you have gained a life!")
    else:
        print("You had nightmares and woke up the same as before...")


def show_map():
    """
    Shows the map to the player and how many lives they have left
    """
    print("Map:\n")
    # one line the assignement and print?
    map_design = draw_map()
    print(map_design)
    # end of one line?
    life = player["life"]
    print(f"\nYou have {life} lives left")


def draw_map():
    """
    Creates the map to be viewed by player
    """
    map_string = ""
    pos = 0
    for x in range(5):
        for y in range(5):
            map_string += (legend[rooms[pos].status])
            pos += 1
        map_string += "\n"
    return map_string


def player_movement_choice():
    """
    Asks for input to move player
    Only gives possible options
    """
    print("Checking possible movements...\n")
    move_up, move_down, move_left, move_right = (True, True, True, True)
    for i in range(25):
        if rooms[i].status == "player":
            move_up = False if i in (0, 1, 2, 3, 4) else True
            move_down = False if i in (20, 21, 22, 23, 24) else True
            move_left = False if i in (0, 5, 10, 15, 20) else True
            move_right = False if i in (4, 9, 14, 19, 24) else True
    print("Would you like to go:")
    if move_up:
        print('"up" to go up')
    if move_down:
        print('"down" to go down')
    if move_left:
        print('"left" to go left')
    if move_right:
        print('"right" to go right')
    direction = input("I want to go...   ")
    if direction not in ("up", "left", "down", "right"):
        print("Wrong input, please try again\n")
        player_movement_choice()
    move_player(direction)


def move_player(direction):
    """
    Moves player if possible
    Otherwise returns to asking direction
    """
    # Needs some work on conditions for movement
    print("Moving player...\n")
#    previous_room = player["room"]
    if direction == "up" and player["room"] > 4:
        rooms[player["room"]].status = "empty"
        player["room"] -= 5
        rooms[player["room"]].status = "player"
    if direction == "down" and player["room"] < 19:
        rooms[player["room"]].status = "empty"
        player["room"] += 5
        rooms[player["room"]].status = "player"
    if direction == "left" and player["room"] not in (0, 5, 10, 15, 20):
        rooms[player["room"]].status = "empty"
        player["room"] -= 1
        rooms[player["room"]].status = "player"
    if direction == "right" and player["room"] not in (4, 9, 14, 19, 24):
        rooms[player["room"]].status = "empty"
        player["room"] += 1
        rooms[player["room"]].status = "player"
#    if player["room"] < 0 or player["room"] > 24:
#        player["room"] = previous_room
#        print("Move impossible, please try again")
#        player_movement_choice()


def check_movement_result():
    """
    Checks what the player has encountered after their move
    """
    print("Checking where you are...\n")
    if player["room"] == door["room"]:
        victory()
    if player["room"] == skel["room"]:
        encounter()


def encounter():
    """
    When player encounters a skeleton
    """
    fight_or_flight = input("You have encountered a skeleton! Would you like \
to fight ('Y') or retreat ('N')?   ")
    if fight_or_flight == "Y":
        fight()
    elif fight_or_flight == "N":
        direction = random.randint(1, 2)
        print(direction)
        if direction == 1:
            print("You failed to escape, you have to fight\n")
            fight()
        elif direction == 2:
            print("You run away...\n")
            player_movement_choice()
    else:
        print("Wrong input, please try again\n")
        encounter()


def fight():
    """
    Fight against skeleton
    """
    print("You fight the skeleton. He hits you first \
but you manage to defeat it!")
    player["life"] -= 1
    rooms[skel["room"]].status = "player"


def victory():
    """
    When player reaches the exit
    Resets player position and life
    """
    print("\n\nYou made it out!\n!!!Congratulations!!!\n\n")
    player["row"], player["column"] = (0, 0)
    player["life"] = 2
    main()


def defeat():
    """
    When player runs out of lives
    Resets player position
    """
    print("\n\nYou died!\n!!!Better luck next time!!!\n\n")
    player["row"], player["column"] = (0, 0)
    player["life"] = 2
    main()


def main():
    """
    Main function, runs the game
    """
    print("Starting game...\n")
    create_map()
    while player["life"]:
        player_action_choice()
        print_positions()
    defeat()


main()
