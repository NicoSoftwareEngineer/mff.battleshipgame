import player
import utils.coordinate as coordinate
import utils.shot_result as shot_result
import utils.cmd_utils as cmd_utils
import utils.random_gen as rnd

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
            self.players.append(player.Player(name, 0))
            
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
                            cmd_utils.clear()
                            self.players[i].ship_board.print()
                            
                            
                    if not was_ship_added:        
                        right_input = True
                        input_coordinates = input("Please enter valid coordinates: \n")
            cmd_utils.clear()
                                        
    def play(self):
        if self.game_type == "a":
            self.two_player_game()
        else:
            self.agains_computer()
        
    def two_player_game(self):
        turn = 0
        has_changed = True
        while not self.has_ended:
            if has_changed:
                print(f"It's {self.players[turn % 2].name} turn to shoot")
            else:
                print(f"{self.players[turn % 2].name} shoots again")
            
            has_changed = self.players[turn % 2].shoot_at(self.players[(turn % 2) + 1])
            if has_changed:
                turn += 1
            self.has_ended = any(all(s.is_sunk for s in p.ships) for p in self.players)
        
        winner = self.players[turn % 2]
        loser = self.players[(turn + 1) % 2]
        self.print_game_results(winner, loser)
        
    def agains_computer(self):
        self.generate_computer_player()
        
        turn = 0
        has_changed = True
        while not self.has_ended:
            if has_changed:
                print(f"It's {self.players[turn % 2].name} turn to shoot")
            else:
                print(f"{self.players[turn % 2].name} shoots again")
            
            has_changed = self.players[turn % 2].shoot_at(self.players[(turn + 1) % 2])
            print(has_changed)
            self.has_ended = any(all(s.is_sunk for s in p.ships) for p in self.players)
            if has_changed and not self.has_ended:
                turn += 1
        
        winner = self.players[turn % 2]
        loser = self.players[(turn + 1) % 2]
        self.print_game_results(winner, loser)
        
    def generate_computer_player(self):
        self.players.append(player.Player(f"Compotadora{len(self.players)}", 1))
        rnd.generate_random_ships_for_player(4, self.players[len(self.players) - 1])
        
                
    def print_game_results(self, winner, loser):
        cmd_utils.clear()
        print(f"The winner is: {winner.name}")
        
        winner.game_board.print_joined(loser.ship_board, f"These are the tried shots of {winner.name}:", f"These are the locations of {loser.name} ships:")
        print()
        loser.game_board.print_joined(winner.ship_board, f"These are the tried shots of {loser.name}:", f"These are the locations of {winner.name} ships:")
            