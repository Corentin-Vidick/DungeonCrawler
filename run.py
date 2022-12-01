"""
Import random function
"""
import random

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


# Create player
player = Entity(0, 2, 1)
skeleton = Entity(random.randint(3, 23), 1, 1)
door = Entity(24, None, None)


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
    rooms[door.pos].status = "door"
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
    if player.pos == door.pos:
        victory()
    elif player.pos == skeleton.pos:
        encounter()
    else:
        no_event()


def no_event():
    """
    When player enters an empty room
    """
    print("\nYou enter the room slowly, trying to look in every direction \
at the same time...\nThe room is safe, but empty\n")


def encounter():
    """
    When player encounters a skeleton
    """
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
    print("\nYou fight the skeleton. He hits you first \
but you manage to defeat it!")
    player.health -= 1
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
        print("\nYou run away...\n")
        player_movement_choice()


def victory():
    """
    When player reaches the exit
    Resets player position and life
    """
    print("\n\nYou made it out!\n!!!Congratulations!!!\n\n")
    player.pos = 0
    player.health = 2
    main()


def defeat():
    """
    When player runs out of lives
    Resets player position
    """
    print("\n\nYou died!\n!!!Better luck next time!!!\n\n")
    player.pos = 0
    player.health = 2
    main()


def main():
    """
    Main function, runs the game
    """
    print("Starting game...\n")
    create_map()
    while player.health:
        player_action_choice()
    defeat()


main()
