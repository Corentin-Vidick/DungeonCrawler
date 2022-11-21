"""
Import random function
"""
import random

# Global variables
player = {
    "row": 3,
    "column": 2,
    "life": 2
}

door = {
    "row": 4,
    "column": 4
}

skel = {
    "row": random.randint(0, 4),
    "column": random.randint(0, 4)
}

legend = {
    "empty": ". ",
    "player": "P ",
    "wall": "# ",
    "skel": "S ",
    "door": "E "
}


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
    print("Creating map...\n")
    global map
    rows, cols = (5, 5)
    map = [["empty" for i in range(cols)] for j in range(rows)]


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
    map_design = draw_map()
    print(map_design)
    life = player["life"]
    print(f"\nYou have {life} lives left")


def draw_map():
    """
    Creates the map to be viewed by player
    """
    design = [[legend["empty"] for x in range(5)] for y in range(5)]
    design[player["row"]][player["column"]] = legend["player"]
    design[skel["row"]][skel["column"]] = legend["skel"]
    design[door["row"]][door["column"]] = legend["door"]
    map_string = ""
    for y in range(5):
        for x in range(5):
            map_string += design[x][y]
        map_string += "\n"
    return map_string


def player_movement_choice():
    """
    Asks for input to move player
    Only gives possible options
    """
    print("Checking possible movements...\n")
    move_up, move_down, move_left, move_right = (True, True, True, True)
    move_up = False if player["row"] == 0 else True
    move_down = False if player["row"] == 4 else True
    move_left = False if player["column"] == 0 else True
    move_right = False if player["column"] == 4 else True
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
    print("Moving player...\n")
    previous_row, previous_column = (player["row"], player["column"])
    if direction == "up":
        player["row"] -= 1
    if direction == "down":
        player["row"] += 1
    if direction == "left":
        player["column"] -= 1
    if direction == "right":
        player["column"] += 1
    if player["row"] < 0 or player["row"] > 4 or\
       player["column"] < 0 or player["column"] > 4:
        player["row"], player["column"] = (previous_row, previous_column)
        print("Move impossible, please try again")
        player_movement_choice()


def check_movement_result():
    """
    Checks what the player has encountered after their move
    """
    print("Checking where you are...\n")
    if player["row"] == door["row"] and player["column"] == door["column"]:
        victory()
    if player["row"] == skel["row"] and player["column"] == skel["column"]:
        encounter()


def encounter():
    """
    When player encounters a skeleton
    """
    fight_or_flight = input("You have encountered a skeleton! Would you like to\
        'Y' fight or 'N' retreat?   ")
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
    print("You fight the skeleton. He hits you first\
but you manage to defeat it!")
    player["life"] -= 1
    skel["row"] = ""
    skel["column"] = ""


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
