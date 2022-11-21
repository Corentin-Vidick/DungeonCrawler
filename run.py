player = {
    "row": 3,
    "column": 2
}

exit = {
    "row": 4,
    "column": 4
}


def print_player_position():
    """
    Temporary function to print player's position
    """
    player_row = player["row"]
    player_column = player["column"]
    print(f"row: {player_row}, column: {player_column}")


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


def victory():
    """
    When player reaches the exit
    Resets player position
    """
    print("\n\nYou made it out!\n!!!Congratulations!!!\n\n")
    player["row"], player["column"] = (0, 0) 
    main()


def main():
    """
    Main function, runs the game
    """
    print("Starting game...\n")
    create_map()
    while 1:
        player_movement_choice()
        if player["row"] == exit["row"] and player["column"] == exit["column"]:
            victory()
        print_player_position()


main()
