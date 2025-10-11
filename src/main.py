
import utils.coordinate as coor
import game
import ship
import player


game_type = input("Would you like to play against another player(a) or a computer(b)\n")
while game_type != "a" and game_type != "b":
    game_type = input("Please enter either 'a' or 'b'\n")

match = game.Game(game_type)

match.setup()

match.play()
