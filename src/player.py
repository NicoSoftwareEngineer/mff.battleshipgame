import ship
import utils.shot_result as shot_result
import utils.cmd_utils as cmd_utils
import utils.coordinate as coordinate
import utils.random_gen as rnd
import utils.aimbot as aimbot
import board
import utils.colors as colors


class Player:
    """Representation of a game participant.

    A `Player` has a name, a list of ships, a player type (human or computer),
    and boards to track own ships and shots made against opponents.
    """
    name = ""
    ships = []
    player_type = 0
    tried_coordinates = []
    game_board = None
    ship_board = None
    
    def __init__(self, name, type):
        """Initialize a Player.

        Args:
            name: display name for the player.
            type: integer player type (0 = human, 1 = computer).
            
        If player is a computer, an `AimBot` instance is created.
        """
        self.ships = []
        self.tried_coordinates = []
        self.name = name
        self.player_type = type
        if(type == 1):
            self.aim_bot = aimbot.AimBot()
        self.game_board = board.Board()
        self.ship_board = board.Board()
        
        
    def add_ship(self, coordinates):
        """Attempt to add a ship for this player.

        Validates coordinates, checks for collisions and touching rules, and
        if valid, registers the ship on this player's ship board.

        Args:
            coordinates: iterable of coordinate strings describing ship cells.

        Returns:
            True if the ship was successfully added, False otherwise.
        """
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
        """Validate and execute a shot against another player.

        Checks if the coordinate was already tried, records the try and
        updates the shooter's game board with hit or miss.

        Args:
            coordinates: coordinate string like '3A'.
            player: the target `Player` instance.

        Returns:
            A `Shot_Result` enum indicating the outcome.
        """
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
        """Perform this player's turn by delegating to human or computer logic."""
        if self.player_type == 0:
            return human_turn([self, target_player])
        else:
            return computer_turn(self, target_player, self.aim_bot)
    
    def did_shot_land(self, shot_coordinates):
        """Check whether a shot hit any of this player's ships.

        Args:
            shot_coordinates: coordinate string representing the attempted shot.

        Returns:
            A `Shot_Result` enum indicating MISS/HIT/SINKED.
        """
        for ship in self.ships:
            result = ship.try_hit(shot_coordinates)
            if bool(result.value):
                return result
    
        return shot_result.Shot_Result(0)
    
    def has_lost(self):
        """Return True if all ships of this player are sunk."""
        return not any(not x.is_sunk for x in self.ship)
    
    def __repr__(self):
        """Return a debug-friendly representation of the player."""
        return f"Player {self.name} of type {self.player_type}"
    
def human_turn(players):
    """Handle a human player's turn.

    Prompts for coordinates, validates them and reports the outcome.

    Args:
        players: two-element list where players[0] is the shooter and players[1]
                 is the target.

    Returns:
        True if turn should pass to the other player, False if the same
        player should act again (e.g. on a hit).
    """
    players[0].game_board.print()
    aimed_coordinates = input("Where do you aim?\n")
    while not coordinate.check_coordinates(aimed_coordinates):
        aimed_coordinates = input("Please enter valid coordinates:\n")
    
    result = players[0].validate_shot_against(aimed_coordinates, players[1])
    cmd_utils.clear()
    match result:
        case shot_result.Shot_Result.MISSED:
            print(colors.ANSI.color_text("You MISSED!", 36))
            return True
            
        case shot_result.Shot_Result.TRIED:
            print("You have already tried this coordinate please try again")
            return False
            
        case shot_result.Shot_Result.HIT:
            print(colors.ANSI.color_text("Success you have hit your opponents ship!", 31))
            return False
        
        case shot_result.Shot_Result.SINKED:
            print(colors.ANSI.color_text("Success you have sinked your opponents ship!", 32))
            return False

def computer_turn(computer, player, aim_bot):
    """Handle a computer player's turn using the provided aim bot.

    The aim bot will fire shots according to its strategy until it should
    stop; the function then prints the computer's game board.

    Args:
        computer: the computer `Player` instance.
        player: the target `Player` instance.
        aim_bot: an `AimBot` instance used to select shots.

    Returns:
        True when the computer's turn is complete.
    """
    result = True
    
    while result:
        result = aim_bot.fire_shot(computer, player)
    computer.game_board.print()
    return True