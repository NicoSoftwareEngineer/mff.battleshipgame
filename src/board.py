import utils.coordinate as coordinate
import utils.colors as colors

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
                tried_coordinate = coordinate.Coordinate(j, chr(i + 65))
                if tried_coordinate in self.missed_coordinates:
                    line += colors.ANSI.color_text( " O ", 36)
                elif tried_coordinate in self.hit_coordinates:
                    line += colors.ANSI.color_text(" X " , 31)
                elif tried_coordinate in self.boat_coordinates:
                    line += colors.ANSI.color_text(" Ψ ", 32)
                else:
                    line += colors.ANSI.color_text(" ~ ", 34)
            
            print(line)

    def print_joined(self, second_board, first_heading = "", second_heading = ""):
        if(first_heading != "" and second_heading != ""):
            print(f"{first_heading} {second_heading}")
        
        print("  0  1  2  3  4  5  6  7  8  9 \t\t  0  1  2  3  4  5  6  7  8  9 ")
        for i in range(10):
            line = f"{chr(i + 65) }"
            for j in range(10):
                tried_coordinate = coordinate.Coordinate(j, chr(i + 65))
                if tried_coordinate in self.missed_coordinates:
                    line += colors.ANSI.color_text(" O ", 36)
                elif tried_coordinate in self.hit_coordinates:
                    line += colors.ANSI.color_text(" X " , 31)
                elif tried_coordinate in self.boat_coordinates:
                    line += colors.ANSI.color_text(" Ψ ", 32)
                else:
                    line += colors.ANSI.color_text(" ~ ", 34)
            line += "\t\t"
            line += f"{chr(i + 65) }"
            for j in range(10):
                tried_coordinate = coordinate.Coordinate(j, chr(i + 65))
                if tried_coordinate in second_board.missed_coordinates:
                    line += colors.ANSI.color_text(" O ", 36)
                elif tried_coordinate in second_board.hit_coordinates:
                    line += colors.ANSI.color_text(" X " , 31)
                elif tried_coordinate in second_board.boat_coordinates:
                    line += colors.ANSI.color_text(" Ψ ", 32)
                else:
                    line += colors.ANSI.color_text(" ~ ", 34)
            
            print(line)


