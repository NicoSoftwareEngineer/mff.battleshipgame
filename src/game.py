import player
import utils.coordinate as coordinate
import utils.shot_result as shot_result
import utils.cmd_utils as cmd_utils

class Game:
    game_type = "a"
    players = []
    has_ended = False
    
    def __init__(self, type):
        self.game_type = type
        self.has_ended = False
    
    def setup(self):
        num_of_players = 2
        if self.game_type != "a":
            num_of_players = 1
            
        for i in range(num_of_players):
            name = input(f"Please enter name of player{i + 1}:\n ")
            self.players.append(player.Player(name, i))
            
        for i in range(len(self.players)):
            cmd_utils.clear()
            input(f"It's {self.players[i].name} turn to choose ship locations. Press enter to continue")
            self.players[i].ship_board.print()
            while len(self.players[i].ships) != 4:
                right_input = True
                was_ship_added = False
                input_coordinates = input("Please enter coordinates of your ship, \n" +
                                              "please enter them in the followint format: \n" +
                                              "'1A 2A' for size 2, '3A 3B 3C 3D' for size 4. "+
                                              "Each player will have 4 ships of size 2, 3, 4, 5.\n")
                while not was_ship_added:
                    splited_coordinates = input_coordinates.split(" ")
                    for coor in splited_coordinates:
                        if len(coor) != 2:
                            right_input &= False    
                            continue 
                        if coordinate.check_coordinates(coor):
                            right_input &= True
                        else:
                            right_input &= False
                    if right_input:
                        was_ship_added = self.players[i].add_ship(splited_coordinates)
                        if was_ship_added:
                            print("Ship was succesfully added\n\n")
                    if not was_ship_added:        
                        right_input = True
                        input_coordinates = input("Please enter valid coordinates: \n")
            cmd_utils.clear()
                                        
    def play(self):
        if self.game_type == "a":
            self.two_player_game()
        
        
    def two_player_game(self):
        turn = 0
        has_changed = True
        while not self.has_ended:
            if has_changed:
                print(f"It's {self.players[turn % 2].name} turn to shoot")
            else:
                print(f"{self.players[turn % 2].name} shoots again")
            self.players[turn % 2].game_board.print()
            aimed_coordinates = input("Where do you aim?\n")
            while not coordinate.check_coordinates(aimed_coordinates):
                aimed_coordinates = input("Please enter valid coordinates:\n")
            
            result = self.players[turn % 2].validate_shot_against(aimed_coordinates, self.players[(turn + 1) % 2])
            cmd_utils.clear()
            
            match result:
                case shot_result.Shot_Result.MISSED:
                    print("You MISSED!")
                    turn += 1
                    has_changed = True
                    
                case shot_result.Shot_Result.TRIED:
                    print("You have already tried this coordinate please try again")
                    has_changed = False
                    
                case shot_result.Shot_Result.HIT:
                    print("Success you have hit your opponents ship!")
                    has_changed = False
                
                case shot_result.Shot_Result.SINKED:
                    print("You have succesfully sinked your opponents ship")
                    has_changed = False
            print()
            self.has_ended = any(all(s.is_sunk for s in p.ships) for p in self.players)
        
        winner = self.players[turn % 2]
        loser = self.players[(turn + 1) % 2]
        self.print_game_results(winner, loser)
                
    def print_game_results(self, winner, loser):
        cmd_utils.clear()
        print(f"The winner is: {winner.name}")
        
        winner.game_board.print_joined(loser.ship_board, f"These are the tried shots of {winner.name}:", f"These are the locations of {loser.name} ships:")
        print()
        loser.game_board.print_joined(winner.ship_board, f"These are the tried shots of {loser.name}:", f"These are the locations of {winner.name} ships:")
            