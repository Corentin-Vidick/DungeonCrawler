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
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] == "player":
                player_row = i
                player_column = j
    move_up = False if player_row == 0 else True
    move_down = False if player_row == 4 else True
    move_left = False if player_column == 0 else True
    move_right = False if player_column == 4 else True
    print("Would you like to go:")
    if move_up:
        print('"up" to go up')
    if move_down:
        print('"down" to go down')
    if move_left:
        print('"left" to go left')
    if move_right:
        print('"right" to go right')
    direction = input("I want to go...")
    return direction


def main():
    """
    Main function, runs the game
    """
    print("Starting game...\n")
    create_map()
    direction = player_movement_choice()


main()
