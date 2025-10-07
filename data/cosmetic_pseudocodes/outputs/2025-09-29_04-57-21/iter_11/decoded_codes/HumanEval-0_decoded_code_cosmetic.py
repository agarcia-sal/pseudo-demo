from typing import Sequence

def has_close_elements(number_sequence: Sequence[int | float], limit: float) -> bool:
    primary_pos: int = 0
    length: int = len(number_sequence)
    while primary_pos < length:
        secondary_pos: int = 0
        while secondary_pos < length:
            if primary_pos != secondary_pos:
                gap: float = number_sequence[secondary_pos] - number_sequence[primary_pos]
                if (0 <= gap < limit) or (gap < 0 and -gap < limit):
                    return True
            secondary_pos += 1
        primary_pos += 1
    return False