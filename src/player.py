import ship
import utils.shot_result as shot_result
import board

class Player:
    name = ""
    ships = []
    order = 0
    tried_coordinates = []
    game_board = board.Board()
    
    def __init__(self, name, order):
        self.ships = []
        self.name = name
        self.order = order
        
    def add_ship(self, coordinates):
        for existingShip in self.ships:
            if(existingShip.check_if_contains_coordinates(coordinates)):
                return False
            elif existingShip.size == len(coordinates):
                return False
            
        self.ships.append(ship.Ship(coordinates))
        return True
        
    def validate_shot(self, coordinates):
        if coordinates in self.tried_coordinates:
            return False
    
        self.tried_coordinates.append(coordinates)
    
        for ship in self.ships:
            result = ship.try_hit(coordinates)
            if bool(result):
                self.game_board.hit_at(coordinates)
                return result
    
        self.game_board.miss_at(coordinates)
        return shot_result.Shot_Result(0)
    
    def has_lost(self):
        return not any(not x.is_sunk for x in self.ship)
    
    def __repr__(self):
        return f"Player {self.name} with these ships {self.ships}"