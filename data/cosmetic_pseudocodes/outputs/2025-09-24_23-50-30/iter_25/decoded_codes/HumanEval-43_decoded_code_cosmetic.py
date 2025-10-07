from typing import Sequence

def pairs_sum_to_zero(sequence: Sequence[int]) -> bool:
    position_x: int = 0
    while position_x < len(sequence):
        value_p: int = sequence[position_x]
        position_y: int = position_x + 1
        while position_y < len(sequence):
            value_q: int = sequence[position_y]
            if (value_p + value_q) == 0:
                return True
            position_y += 1
        position_x += 1
    return False