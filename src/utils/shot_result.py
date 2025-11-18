from enum import Enum


class Shot_Result(Enum):
    """Enumeration of possible shot outcomes.

    Values:
        MISSED: shot did not hit any ship.
        HIT: shot hit a ship but did not sink it.
        SINKED: shot sank a ship.
        TRIED: coordinate was already attempted.
    """
    MISSED = 0
    HIT = 1
    SINKED = 2
    TRIED = 3