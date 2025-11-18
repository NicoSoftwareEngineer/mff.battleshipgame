"""Unit tests for coordinate creation, hits, and validation."""

import utils.coordinate as coordinate

def test_coordinate_creation():
    """Coordinates store provided x/y values and default to not hit."""
    coor = coordinate.Coordinate('3', 'A')
    assert coor.x_cor == '3'
    assert coor.y_cor == 'A'
    assert not coor.was_hit
    
def test_coordinate_hit():
    """`hit` toggles `was_hit` only when both axis values match."""
    coor = coordinate.Coordinate('5', 'D')
    assert not coor.was_hit
    hit_result = coor.hit('5', 'D')
    assert hit_result
    assert coor.was_hit
    miss_result = coor.hit('4', 'D')
    assert not miss_result
    assert coor.was_hit

def test_coordinate_validation():
    """`check_coordinates` enforces digit+letter format within board bounds."""
    assert coordinate.check_coordinates('3A')
    assert not coordinate.check_coordinates('10A')
    assert not coordinate.check_coordinates('3K')
    assert not coordinate.check_coordinates('AA')

