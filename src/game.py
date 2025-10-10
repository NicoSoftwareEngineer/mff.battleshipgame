import player
import utils.coordinate as coordinate

class Game:
    game_type = "a"
    players = []
    
    def __init__(self, type):
        self.game_type = type
    
    def setup(self):
        for i in range(2):
            name = input(f"Please enter name of player{i + 1}:\n ")
            self.players.append(player.Player(name, i))
        print(len(self.players))
        for i in range(len(self.players)):
            print(i)
            print(self.players[i])
            while len(self.players[i].ships) != 2:
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
                        if not was_ship_added:
                            print("You either already have a ship at the inputed coordinates or you already have a ship of that size, please try again")
                                                    
                        else:
                            print(f"Ship was added to {self.players[i].name} \n\n\n")
                    if not was_ship_added:        
                        right_input = True
                        input_coordinates = input("Please enter valid coordinates: \n")
                                        
                        
                            
                
            