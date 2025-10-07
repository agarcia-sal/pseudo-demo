from typing import Sequence
import math


def has_close_elements(array_alpha: Sequence[float], delta_beta: float) -> bool:
    pointer_x: int = 0
    length: int = len(array_alpha)
    while pointer_x < length:
        pointer_y: int = 0
        while pointer_y < length:
            if pointer_x != pointer_y:
                diff = array_alpha[pointer_x] - array_alpha[pointer_y]
                gap_gamma = diff * math.copysign(1, diff)  # effectively abs(diff), preserving float type correctly
                if gap_gamma < delta_beta:
                    return True
            pointer_y += 1
        pointer_x += 1
    return False