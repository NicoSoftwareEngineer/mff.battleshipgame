import utils.coordinate as coordinate

class Board:
    missed_coordinates = None
    hit_coordinates = None
    boat_coordinates = None
    
    def __init__(self):
        self.missed_coordinates = []
        self.hit_coordinates = []
        self.boat_coordinates = []
    
    def hit_at(self, coordinates):
        self.hit_coordinates.append(coordinate.Coordinate(coordinates[0], coordinates[1]))
        
    def miss_at(self, coordinates):
        self.missed_coordinates.append(coordinate.Coordinate(coordinates[0], coordinates[1]))
        
    def ship_at(self, coordinates):
        for coor in coordinates:
            self.boat_coordinates.append(coordinate.Coordinate(coor[0], coor[1]))
                    
        
    def print(self):
        print("  0  1  2  3  4  5  6  7  8  9")
        for i in range(10):
            line = f"{chr(i + 65) }"
            for j in range(10):
                tried_coordinate = coordinate.Coordinate(i, chr(j + 65))
                if tried_coordinate in self.missed_coordinates:
                    line += " O "
                elif tried_coordinate in self.hit_coordinates:
                    line += " X "
                elif tried_coordinate in self.boat_coordinates:
                    line += " Ψ "
                else:
                    line += " ~ "
            print(line)
        