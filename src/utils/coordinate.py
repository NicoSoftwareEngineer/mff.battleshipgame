class Coordinate:
    x_cor = ""
    y_cor = ""
    was_hit = False
    
    def __init__(self, x, y):
        self.x_cor = x
        self.y_cor = y
        
    def __eq__(self, value):
        return (str(self.x_cor) == str(value.x_cor) and str(self.y_cor) == str(value.y_cor))
    
    def __repr__(self):
        return f"Coordinates: {self.x_cor}, {self.y_cor}"
        
    def hit(self, x, y):
        if(x == self.x_cor and y == self.y_cor):
            self.was_hit = True
            return True
        
        return False

def check_coordinates(coordinates):
    if len(coordinates) != 2:
        return False
    
    if ord(coordinates[0]) < 48 or ord(coordinates[0]) > 57:
        return False
    
    if ord(coordinates[1]) < 65 or ord(coordinates[1]) > 74:
        return False
    
    return True