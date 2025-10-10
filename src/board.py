import utils.coordinate as coordinate

class Board:
    missed_coordinates = []
    hit_coordinates = []
    
    def hit_at(self, coordinates):
        self.hit_coordinates.append(coordinate.Coordinate(coordinates[0], coordinates[1]))
        
    def miss_at(self, coordinates):
        self.missed_coordinates.append(coordinate.Coordinate(coordinates[0], coordinates[1]))
        
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
                else:
                    line += " - "
            print(line)
        