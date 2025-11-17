import utils.random_gen as rnd_gen
import utils.shot_result as shot_result


class AimBot:
    last_successful_shot = None
    known_direction = None
    tried_coordinates = []
    coor_direction_tactic = True #1 - increase coor from last_suc_shot 0 - decrease coor from last_suc_shot
    
    def __init__(self):
        self.last_successful_shot = None
        self.known_direction = None
        self.tried_coordinates = []
        self.hit_min_limit = False
        self.hit_max_limit = False
    
    def fire_shot(self, computer, player):
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
        coor_to_shoot_at = self.get_next_coor_with_vertical_direction()
        should_continue = self.shoot(computer, player, coor_to_shoot_at)

        if not should_continue:
            self.coor_direction_tactic = not self.coor_direction_tactic
        
        return should_continue

    def shoot_with_horizontal_direction(self, computer, player):
        coor_to_shoot_at = self.get_next_coor_with_horizontal_direction()
        should_continue = self.shoot(computer, player, coor_to_shoot_at)

        if not should_continue:
            self.coor_direction_tactic = not self.coor_direction_tactic

        return should_continue

    def shoot_without_hit(self, computer, player):
        coor_to_shoot_at = self.get_next_random_coor()
        should_continue = self.shoot(computer, player, coor_to_shoot_at)
        return should_continue
    
    def shoot_without_direction(self, computer, player):
        coor_to_shoot_at = self.get_next_coor_without_direction()
        should_continue = self.shoot(computer, player, coor_to_shoot_at)
        return should_continue
    
    def get_next_coor_without_direction(self):
        possible_coords = [f"{chr(ord(self.last_successful_shot[0])- 1)}{self.last_successful_shot[1]}", 
                           f"{chr(ord(self.last_successful_shot[0]) + 1)}{self.last_successful_shot[1]}", 
                           f"{self.last_successful_shot[0]}{chr(ord(self.last_successful_shot[1]) + 1)}", 
                           f"{self.last_successful_shot[0]}{chr(ord(self.last_successful_shot[1]) - 1)}"]
        
        for coor in possible_coords:
            if not coor in self.tried_coordinates:
                return coor
    
    def get_next_coor_with_vertical_direction(self):
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
        coor_to_shoot_at = rnd_gen.generate_random_coordinate()
        while coor_to_shoot_at in self.tried_coordinates:
            coor_to_shoot_at = rnd_gen.generate_random_coordinate()
        return coor_to_shoot_at
    
    def get_direction(self, next_coor):
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
        result_shot = computer.validate_shot_against(coor_to_shoot_at, player)
        if(result_shot is shot_result.Shot_Result.SINKED):
            self.last_successful_shot = None
            self.known_direction = None
            self.coor_direction_tactic = True
        if(result_shot is shot_result.Shot_Result.HIT):
            self.get_direction(coor_to_shoot_at)
        self.tried_coordinates.append(coor_to_shoot_at)
        return bool(result_shot.value)