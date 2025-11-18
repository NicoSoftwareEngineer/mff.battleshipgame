"""Unit tests covering `ship.Ship` behaviors and helpers."""

import ship
import utils.shot_result as shot_result

def test_ship_creation():
    """Ships remember initial size and coordinate count upon creation."""
    ship_instance = ship.Ship(['1A', '1B', '1C'])
    assert ship_instance.size == 3
    assert len(ship_instance.coordinates) == 3
    assert not ship_instance.is_sunk
    
def test_ship_try_hit_and_sinking():
    """`try_hit` returns HIT then SINKED as each segment is destroyed."""
    ship_instance = ship.Ship(['2A', '2B'])
    result1 = ship_instance.try_hit('2A')
    assert result1 == shot_result.Shot_Result.HIT
    assert not ship_instance.is_sunk
    result2 = ship_instance.try_hit('2B')
    assert result2 == shot_result.Shot_Result.SINKED
    assert ship_instance.is_sunk

def test_ship_check_if_contains_coordinates():
    """`check_if_contains_coordinates` detects matching coordinates only."""
    ship_instance = ship.Ship(['3A', '3B', '3C'])
    assert ship_instance.check_if_contains_coordinates(['3B'])
    assert not ship_instance.check_if_contains_coordinates(['4A'])

def test_ship_creation_on_invalid_coordinates():
    """Coordinate validation rejects out-of-range cells but accepts valid ones."""
    assert not ship.check_if_coordinates_are_valid_for_ship(['10A', '3K']) 
    assert ship.check_if_coordinates_are_valid_for_ship(['5A', '5B', '5C'])
    
def test_ship_touching():
    """Touching logic returns True for adjacent ships and False otherwise."""
    ship1 = ship.Ship(['4A', '4B', '4C'])
    ship2 = ship.Ship(['4D', '4E', '4F'])
    ship3 = ship.Ship(['5A', '5B', '5C'])
    assert ship1.check_if_is_touching(ship2)
    assert ship1.check_if_is_touching(ship3)
    assert not ship2.check_if_is_touching(ship3)