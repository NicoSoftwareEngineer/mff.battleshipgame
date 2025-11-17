import ship
import utils.shot_result as shot_result
import utils.cmd_utils as cmd_utils
import utils.coordinate as coordinate
import utils.random_gen as rnd
import utils.aimbot as aimbot
import board

class Player:
    name = ""
    ships = []
    player_type = 0
    tried_coordinates = []
    game_board = None
    ship_board = None
    
    def __init__(self, name, type):
        self.ships = []
        self.tried_coordinates = []
        self.name = name
        self.player_type = type
        if(type == 1):
            self.aim_bot = aimbot.AimBot()
        self.game_board = board.Board()
        self.ship_board = board.Board()
        
        
    def add_ship(self, coordinates):
        ship_to_add = ship.Ship(coordinates)
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
            elif existingShip.check_if_is_touching(ship_to_add):
                print("Two ships cannot be touching!")
                return False
            
        self.ships.append(ship_to_add)
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
    
    def shoot_at(self, target_player):
        print(f"{self} shoots at {target_player}")
        if self.player_type == 0:
            return human_turn([self, target_player])
        else:
            return computer_turn(self, target_player, self.aim_bot)
    
    def did_shot_land(self, shot_coordinates):
        for ship in self.ships:
            result = ship.try_hit(shot_coordinates)
            if bool(result.value):
                return result
    
        return shot_result.Shot_Result(0)
    
    def has_lost(self):
        return not any(not x.is_sunk for x in self.ship)
    
    def __repr__(self):
        return f"Player {self.name} of type {self.player_type}"
    
def human_turn(players):
    players[0].game_board.print()
    aimed_coordinates = input("Where do you aim?\n")
    while not coordinate.check_coordinates(aimed_coordinates):
        aimed_coordinates = input("Please enter valid coordinates:\n")
    
    result = players[0].validate_shot_against(aimed_coordinates, players[1])
    cmd_utils.clear()
    match result:
        case shot_result.Shot_Result.MISSED:
            print("You MISSED!")
            return True
            
        case shot_result.Shot_Result.TRIED:
            print("You have already tried this coordinate please try again")
            return False
            
        case shot_result.Shot_Result.HIT:
            print("Success you have hit your opponents ship!")
            return False
        
        case shot_result.Shot_Result.SINKED:
            print("You have succesfully sinked your opponents ship")
            return False

def computer_turn(computer, player, aim_bot):
    result = True
    
    while result:
        result = aim_bot.fire_shot(computer, player)
    computer.game_board.print()
    return True