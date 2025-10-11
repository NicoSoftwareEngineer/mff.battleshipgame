import ship
import utils.shot_result as shot_result
import board

class Player:
    name = ""
    ships = []
    order = 0
    tried_coordinates = []
    game_board = None
    ship_board = None
    
    def __init__(self, name, order):
        self.ships = []
        self.tried_coordinates = []
        self.name = name
        self.order = order
        self.game_board = board.Board()
        self.ship_board = board.Board()
        
    def add_ship(self, coordinates):
        if not ship.check_if_coordinates_are_valid_for_ship(coordinates):
            print("These are invalid coordinates for a ship")
            return
        for existingShip in self.ships:
            if(existingShip.check_if_contains_coordinates(coordinates)):
                print("You already have a ship on these coordinates!")
                return False
            elif existingShip.size == len(coordinates):
                print("You already have a ship this size!")
                return False
            
        self.ships.append(ship.Ship(coordinates))
        self.ship_board.ship_at(coordinates)
        return True
        
    def validate_shot_against(self, coordinates, player):
        if coordinates in self.tried_coordinates:
            return shot_result.Shot_Result.TRIED
    
        self.tried_coordinates.append(coordinates)

        result = player.did_shot_land(coordinates)
        if(bool(result.value)):
            self.game_board.hit_at(coordinates)
        else:
            self.game_board.miss_at(coordinates)
        
        return result
    
    def did_shot_land(self, shot_coordinates):
        for ship in self.ships:
            result = ship.try_hit(shot_coordinates)
            if bool(result.value):
                return result
    
        return shot_result.Shot_Result(0)
    
    def has_lost(self):
        return not any(not x.is_sunk for x in self.ship)
    
    def __repr__(self):
        return f"Player {self.name} with these ships {self.ships}"