class Coordinate:
    """Immutable-like value object representing a single board cell.

    Attributes:
        x_cor: column identifier (number or char depending on usage).
        y_cor: row identifier (character like 'A').
        was_hit: boolean tracking whether this coordinate was hit.
    """
    x_cor = ""
    y_cor = ""
    was_hit = False
    
    def __init__(self, x, y):
        """Create a Coordinate with column `x` and row `y`."""
        self.x_cor = x
        self.y_cor = y
        
    def __eq__(self, value):
        """Equality comparison used to determine coordinate identity."""
        return (str(self.x_cor) == str(value.x_cor) and str(self.y_cor) == str(value.y_cor))
    
    def __repr__(self):
        """Return a concise string representation for debugging."""
        return f"Coordinates: {self.x_cor}, {self.y_cor}"
        
    def hit(self, x, y):
        """Mark the coordinate as hit if the provided x,y match.

        Args:
            x: column identifier of the attempted shot.
            y: row identifier of the attempted shot.

        Returns:
            True if this coordinate was hit, False otherwise.
        """
        if(x == self.x_cor and y == self.y_cor):
            self.was_hit = True
            return True
        
        return False

def check_coordinates(coordinates):
    """Quick validation for coordinate strings like '3A'.

    Returns True for well-formed coordinates within the board range
    (columns 0-9 and rows A-J), False otherwise.
    """
    if len(coordinates) != 2:
        return False
    
    if ord(coordinates[0]) < 48 or ord(coordinates[0]) > 57:
        return False
    
    if ord(coordinates[1]) < 65 or ord(coordinates[1]) > 74:
        return False
    
    return True