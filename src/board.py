import utils.coordinate as coordinate
import utils.colors as colors

class Board:
    """Represent a 10x10 board for a Battleship player.

    The board tracks missed shots, successful hits and ship coordinates
    (boat locations). Coordinates are stored as `Coordinate` objects from
    `utils.coordinate`.
    """
    missed_coordinates = None
    hit_coordinates = None
    boat_coordinates = None
    
    def __init__(self):
        """Create an empty board with no hits, misses or ships recorded."""
        self.missed_coordinates = []
        self.hit_coordinates = []
        self.boat_coordinates = []
    
    def hit_at(self, coordinates):
        """Record a successful hit at the given coordinates.

        Args:
            coordinates: Two-element sequence XY where x is column and y is row.
        """
        self.hit_coordinates.append(coordinate.Coordinate(coordinates[0], coordinates[1]))
        
    def miss_at(self, coordinates):
        """Record a missed shot at the given coordinates.

        Args:
            coordinates: Two-element sequence XY where x is column and y is row.
        """
        self.missed_coordinates.append(coordinate.Coordinate(coordinates[0], coordinates[1]))
        
    def ship_at(self, coordinates):
        """Mark a set of coordinates as occupied by a ship.

        Args:
            coordinates: iterable of two-element sequences representing ship cells.
        """
        for coor in coordinates:
            self.boat_coordinates.append(coordinate.Coordinate(coor[0], coor[1]))
                    
        
    def print(self):
        """Render the board to stdout using colored symbols.

        Symbols denote misses, hits, ship locations or water. This method
        prints a labeled 10x10 grid.
        """
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
        """Print two boards side-by-side for comparison.

        Useful for showing tried shots alongside the opponent's ship locations.

        Args:
            second_board: another `Board` instance to print next to this one.
            first_heading: optional heading printed above the first board.
            second_heading: optional heading printed above the second board.
        """
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


