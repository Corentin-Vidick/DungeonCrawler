player = {
    """
    Defines starting position of player
    Makes player's position available throughout program
    """
    "row": 3,
    "column": 2
}


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
    map[2][2] = "player"
    map[4][4] = "exit"


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
    if direction != "up" and "down" and "left" and "right":
        print("Wrong input, please try again\n")
        player_movement_choice()
    return direction


def move_player(direction):
    """
    Moves player if possible
    Otherwise returns to asking direction
    """
    print("Moving player...")
    print(direction)


def main():
    """
    Main function, runs the game
    """
    print("Starting game...\n")
    create_map()
    direction = player_movement_choice()
    move_player(direction)


main()
