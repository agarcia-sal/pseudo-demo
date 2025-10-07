from typing import Sequence

def has_close_elements(array_alpha: Sequence[int], limit_beta: int) -> bool:
    position_gamma: int = 0
    length: int = len(array_alpha)
    while position_gamma < length:
        pointer_delta: int = 0
        while pointer_delta < length:
            if position_gamma != pointer_delta:
                gap_epsilon: int = abs(array_alpha[position_gamma] - array_alpha[pointer_delta])
                if limit_beta > gap_epsilon:
                    return True
            pointer_delta += 1
        position_gamma += 1
    return False