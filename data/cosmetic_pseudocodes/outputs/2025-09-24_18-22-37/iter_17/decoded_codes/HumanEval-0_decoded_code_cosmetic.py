from typing import Sequence

def has_close_elements(container: Sequence[float], delta: float) -> bool:
    pos_a = 0
    length = len(container)
    while pos_a < length:
        val_a = container[pos_a]
        pos_b = 0
        while pos_b < length:
            val_b = container[pos_b]
            if pos_a == pos_b:
                pos_b += 1
                continue
            diff = val_a - val_b
            if diff < 0:
                diff = -diff
            if diff < delta:
                return True
            pos_b += 1
        pos_a += 1
    return False