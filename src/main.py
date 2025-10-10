
import utils.coordinate as coor
import game
import ship


game_type = input("Would you like to play against another player(a) or a computer(b)\n")
while game_type != "a" and game_type != "b":
    game_type = input("Please enter either 'a' or 'b'\n")



# match = game.Game(game_type)

# match.setup()

# print(match.players[0])
# print(match.players[1])

# print(ord("5"))
# print(ord("A"))
# print((ord("5") < 48 or ord("5") > 57))
# print((ord("A") < 65 or ord("A") > 74))


print(ship.check_if_coordinates_are_valid_for_ship(["1A", "2A", "3A"]))
print(ship.check_if_coordinates_are_valid_for_ship(["1A", "1B", "1C"]))
print(ship.check_if_coordinates_are_valid_for_ship(["1A", "1B", "1D"]))
print(ship.check_if_coordinates_are_valid_for_ship(["1A", "2A", "4A"]))
