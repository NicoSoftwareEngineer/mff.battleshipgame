import random
import ship
import utils.cmd_utils as cmd_utils

def generate_random_ships_for_player(number_of_ships, player):
    """Generate and adds `number_of_ships` amount of random ships for `player`.

    Ships are created with increasing sizes starting at 2. The function
    repeatedly attempts random placements until the requested count is
    reached, then clears the terminal.
    """
    while len(player.ships) != number_of_ships:
        was_ship_added = False
        while not was_ship_added:
            was_ship_added = player.add_ship(generate_random_ship_coordinates((2 + len(player.ships))))
    cmd_utils.clear()

def generate_random_ship_coordinates(length):
    """Generate a list of coordinate strings for a ship.

    Args:
        length: desired ship length (integer).

    Returns:
        A list of coordinate strings representing a valid ship placement.
    """
    coordinates_valid = False
    coors = []
    while not coordinates_valid:
        coors = [generate_random_coordinate()]
        direction = random.randint(0,1)
        for i in range(1, length):
            if bool(direction):
                coors.append(f"{chr(ord(coors[0][0] ) + i)}{coors[0][1]}")
            else:
                coors.append(f"{coors[0][0]}{chr(ord(coors[0][1] ) + i)}")
        coordinates_valid = ship.check_if_coordinates_are_valid_for_ship(coors)
    return coors
    
def generate_random_coordinate():
    """Return a single random coordinate string inside the 10x10 board.

    The returned string has the format 'xY' where x is 0-9 and Y is 'A'-'J'.
    """
    x_cor = random.randint(0,9)
    y_cor = random.randint(0,9) + 65
    return f"{x_cor}{chr(y_cor)}"
