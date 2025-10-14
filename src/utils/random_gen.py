import random
import ship
import utils.cmd_utils as cmd_utils

def generate_random_ships_for_player(number_of_ships, player):
    while len(player.ships) != number_of_ships:
        was_ship_added = False
        while not was_ship_added:
            was_ship_added = player.add_ship(generate_random_ship_coordinates((2 + len(player.ships))))
    cmd_utils.Utils.clear()

def generate_random_ship_coordinates(length):
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
    x_cor = random.randint(0,9)
    y_cor = random.randint(0,9) + 65
    return f"{x_cor}{chr(y_cor)}"
