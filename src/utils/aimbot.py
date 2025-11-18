import utils.random_gen as rnd_gen
import utils.shot_result as shot_result


class AimBot:
    """AimBot implements a simple targeting strategy for the computer player.

    The bot remembers its last successful shot and attempts to continue
    shooting in the same line (horizontal or vertical) until a ship is sunk.
    It also tracks all tried coordinates to avoid repeating shots.
    """
    last_successful_shot = None
    known_direction = None
    tried_coordinates = []
    coor_direction_tactic = True #1 - increase coor from last_suc_shot 0 - decrease coor from last_suc_shot
    
    def __init__(self):
        """Initialize AimBot internal state.

        All attributes are reset so the bot starts without any knowledge
        of previous shots or directions.
        """
        self.last_successful_shot = None
        self.known_direction = None
        self.tried_coordinates = []
        self.hit_min_limit = False
        self.hit_max_limit = False
    
    def fire_shot(self, computer, player):
        """Fire shots until the it misses.

        The method uses internal state to decide whether to fire randomly,
        continue along a known direction, or probe around the last hit.

        Args:
            computer: the `Player` instance representing the bot.
            player: the opposing `Player` instance to target.

        Returns:
            False always (the game loop that calls this method handles
            turn advancement). The bot updates boards and internal state
            as a side effect.
        """
        should_continue = True
        while(should_continue):
            if(self.last_successful_shot == None):
                should_continue = self.shoot_without_hit(computer, player)
            else:
                match self.known_direction:
                    case True: #---
                        should_continue = self.shoot_with_horizontal_direction(computer, player)
                    case False: #|
                        should_continue =  self.shoot_with_vertical_direction(computer, player)
                    case None: #unkown
                        should_continue = self.shoot_without_direction(computer, player)
            if(should_continue):
                print("Hit")
        return False

    def shoot_with_vertical_direction(self, computer, player):
        """Attempt a shot following a known vertical direction.

        Chooses the next coordinate along the vertical line determined by
        `last_successful_shot` and delegates to `shoot`.
        """
        coor_to_shoot_at = self.get_next_coor_with_vertical_direction()
        should_continue = self.shoot(computer, player, coor_to_shoot_at)

        if not should_continue:
            self.coor_direction_tactic = not self.coor_direction_tactic
        
        return should_continue

    def shoot_with_horizontal_direction(self, computer, player):
        """Attempt a shot following a known horizontal direction.

        Chooses the next coordinate along the horizontal line determined by
        `last_successful_shot` and delegates to `shoot`.
        """
        coor_to_shoot_at = self.get_next_coor_with_horizontal_direction()
        should_continue = self.shoot(computer, player, coor_to_shoot_at)

        if not should_continue:
            self.coor_direction_tactic = not self.coor_direction_tactic

        return should_continue

    def shoot_without_hit(self, computer, player):
        """Choose a random unused coordinate and fire at it.

        This tactic is used when there is no recent successful hit to
        continue from.
        """
        coor_to_shoot_at = self.get_next_random_coor()
        should_continue = self.shoot(computer, player, coor_to_shoot_at)
        return should_continue
    
    def shoot_without_direction(self, computer, player):
        """Probe coordinates adjacent to the last successful hit.

        Used when there is a last hit but no known orientation of the ship
        yet.
        """
        coor_to_shoot_at = self.get_next_coor_without_direction()
        should_continue = self.shoot(computer, player, coor_to_shoot_at)
        return should_continue
    
    def get_next_coor_without_direction(self):
        """Return an adjacent coordinate (not yet tried) around the last hit.

        The returned coordinate is one of the four orthogonally adjacent
        positions to `last_successful_shot` that was not tried yet.
        """
        possible_coords = [f"{chr(ord(self.last_successful_shot[0])- 1)}{self.last_successful_shot[1]}", 
                           f"{chr(ord(self.last_successful_shot[0]) + 1)}{self.last_successful_shot[1]}", 
                           f"{self.last_successful_shot[0]}{chr(ord(self.last_successful_shot[1]) + 1)}", 
                           f"{self.last_successful_shot[0]}{chr(ord(self.last_successful_shot[1]) - 1)}"]
        
        for coor in possible_coords:
            if not coor in self.tried_coordinates:
                return coor
    
    def get_next_coor_with_vertical_direction(self):
        """Return the next coordinate along a vertical direction from last hit.

        The function walks forward (or backward) from `last_successful_shot`
        until it finds an untried coordinate.
        """
        #|
        y_coor = ord(self.last_successful_shot[1]) + 1
        next_in_line = f"{self.last_successful_shot[0]}{chr(y_coor)}"
        if(next_in_line not in self.tried_coordinates):
            return next_in_line
        
        while(next_in_line in self.tried_coordinates):
            if(self.coor_direction_tactic):
                y_coor += 1
            else:
                y_coor -= 1
                
            next_in_line = f"{self.last_successful_shot[0]}{chr(y_coor)}"
        return next_in_line
        
    def get_next_coor_with_horizontal_direction(self):
        """Return the next coordinate along a horizontal direction from last hit.

        The function walks forward (or backward) from `last_successful_shot`
        until it finds an untried coordinate.
        """
        #----
        x_coor = ord(self.last_successful_shot[0]) + 1
        next_in_line = f"{chr(x_coor)}{self.last_successful_shot[1]}"
        if(next_in_line not in self.tried_coordinates):
            return next_in_line
        
        while(next_in_line in self.tried_coordinates):
            if self.coor_direction_tactic:
               x_coor += 1
            else:
               x_coor -= 1
               
            next_in_line = f"{chr(x_coor)}{self.last_successful_shot[1]}"
        return next_in_line
    
    def get_next_random_coor(self):
        """Return a random unused coordinate.

        The coordinate is generated using `utils.random_gen.generate_random_coordinate`
        and guaranteed to not be present in `tried_coordinates`.
        """
        coor_to_shoot_at = rnd_gen.generate_random_coordinate()
        while coor_to_shoot_at in self.tried_coordinates:
            coor_to_shoot_at = rnd_gen.generate_random_coordinate()
        return coor_to_shoot_at
    
    def get_direction(self, next_coor):
        """Infer the orientation (horizontal/vertical) from two hits.

        If `last_successful_shot` is not set it will be initialized with
        `next_coor`. Otherwise `known_direction` is updated to True for
        horizontal, False for vertical, or None if unclear.
        """
        if(self.last_successful_shot is None):
            self.last_successful_shot = next_coor
            return
        if(self.last_successful_shot[0] == next_coor[0]):#|
            self.known_direction = False
            return 
        if(self.last_successful_shot[1] == next_coor[1]):
            self.known_direction = True
            return
        self.known_direction = None
            
    def shoot(self, computer, player, coor_to_shoot_at):
        """Execute a shot at `coor_to_shoot_at` and update bot state.

        Args:
            computer: the bot `Player` instance (the shooter).
            player: the target `Player` instance.
            coor_to_shoot_at: coordinate string like '3A'.

        Returns:
            True if the shot produced a result that allows the bot to keep
            shooting (e.g. a hit), False otherwise.
        """
        result_shot = computer.validate_shot_against(coor_to_shoot_at, player)
        if(result_shot is shot_result.Shot_Result.SINKED):
            self.last_successful_shot = None
            self.known_direction = None
            self.coor_direction_tactic = True
        if(result_shot is shot_result.Shot_Result.HIT):
            self.get_direction(coor_to_shoot_at)
        self.tried_coordinates.append(coor_to_shoot_at)
        return bool(result_shot.value)