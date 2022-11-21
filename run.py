def create_map():
    """
    Creates map array
    Initialise player position
    Initialise exit position
    """
    print("Creating map")
    global map
    rows, cols = (5, 5)
    map = [["empty" for i in range(cols)] for j in range(rows)]
    map[0][0] = "player"
    map[4][4] = "exit"
    print(map)


def main():
    """
    Main function, runs the game
    """
    print("Start game")
    create_map()


main()
