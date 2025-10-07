from typing import Sequence

def has_close_elements(container: Sequence[float], limit: float) -> bool:
    position_a = 0
    length = len(container)
    while position_a < length:
        value_a = container[position_a]
        position_b = 0
        while position_b < length:
            if position_a == position_b:
                position_b += 1
                continue
            value_b = container[position_b]
            diff = value_a - value_b
            abs_diff = -diff if diff < 0 else diff
            if abs_diff < limit:
                return True
            position_b += 1
        position_a += 1
    return False