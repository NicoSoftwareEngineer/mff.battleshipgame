import utils.coordinate as coordinate
import utils.shot_result as shot_result

class Ship:
    """Model of a ship consisting of coordinates.

    A `Ship` stores its coordinates as `Coordinate` objects, knows its size
    and whether it has been sunk.
    """
    size = 0
    coordinates = []
    is_sunk = False
    
    def __init__(self, coordinates):
        """Initialize a Ship from a sequence of coordinate strings.

        Args:
            coordinates: iterable of coordinate strings (e.g. '3A').
        """
        self.size = len(coordinates)
        self.coordinates = []
        self.is_sunk = False
        for coor in coordinates:
            self.coordinates.append(coordinate.Coordinate(coor[0], coor[1]))
        
    def try_hit(self, tried_coordinates):
        """Attempt to apply a shot to this ship.

        Args:
            tried_coordinates: coordinate string like '3A'.

        Returns:
            A `Shot_Result` indicating MISS/HIT/SINKED.
        """
        result = False
        for coor in self.coordinates:
            result |= coor.hit(tried_coordinates[0], tried_coordinates[1])
        
        if self.check_if_sunked() and result:
            self.is_sunk = True
            return shot_result.Shot_Result.SINKED
        
        return shot_result.Shot_Result(int(result))
        
    def check_if_sunked(self):
        """Return True if every coordinate of this ship was hit."""
        result = True
        for coor in self.coordinates:
            result &= coor.was_hit
        
        return result
    
    def check_if_contains_coordinates(self, coordinates):
        """Return True if any of the provided coordinates belong to this ship.

        Args:
            coordinates: iterable of coordinate strings to test.
        """
        for coor in coordinates:
            try_coor = coordinate.Coordinate(coor[0], coor[1])
            if try_coor in self.coordinates:
                return True
            
        return False
    
    def check_if_is_touching(self, ship):
        """Check whether this ship touches another ship.

        Touching is defined as any ship cell being adjacent (N/S/E/W)
        to any cell of the other ship.
        """
        is_touching = False
        for coord in self.coordinates:
            arr = [f"{coord.x_cor}{coord.y_cor}",
                   f"{chr(ord(coord.x_cor)- 1)}{coord.y_cor}",
                   f"{chr(ord(coord.x_cor) + 1)}{coord.y_cor}", 
                   f"{coord.x_cor}{chr(ord(coord.y_cor) + 1)}",
                   f"{coord.x_cor}{chr(ord(coord.y_cor) - 1)}"]
            
            is_touching |= ship.check_if_contains_coordinates(arr)
        return is_touching
    
    def __repr__(self):
        """Return a readable representation useful for debugging."""
        return f"Ship of size {self.size}, is {self.is_sunk} sunked, with these coordinates {self.coordinates}"

def check_if_coordinates_are_valid_for_ship(coordinates):
    """Validate whether a sequence of coordinate strings forms a valid ship.

    A valid ship is contiguous either horizontally or vertically with
    consistent increments of one cell.

    Args:
        coordinates: iterable of coordinate strings to validate.

    Returns:
        True if coordinates form a valid ship placement, False otherwise.
    """
    last_coordinates_checked = ""
    direction = 0
    for coor in coordinates:
        if not coordinate.check_coordinates(coor):
            return False
        
        match direction:
            case 1: #vertically x-same y-bigger by one
                if last_coordinates_checked[0] != coor[0]:
                    return False
                if ord(last_coordinates_checked[1]) + 1 == ord(coor[1]):
                    last_coordinates_checked = coor
                    continue
                else:
                    return False
            case 2: #horizotnaly y-same x-bigger by one
                if last_coordinates_checked[1] != coor[1]:
                    return False
                if ord(last_coordinates_checked[0]) + 1 == ord(coor[0]):
                    last_coordinates_checked = coor
                    continue
                else:
                    return False
            case _:
                if last_coordinates_checked == "":
                    last_coordinates_checked = coor
                    continue
                if direction == 0:
                    if ord(last_coordinates_checked[0]) + 1 == ord(coor[0]) and last_coordinates_checked[0] != coor[0]:
                        direction = 2
                        
                    if ord(last_coordinates_checked[1]) + 1 == ord(coor[1]) and last_coordinates_checked[1] != coor[1]:
                        direction = 1
                    last_coordinates_checked = coor
                        
    return bool(direction) 