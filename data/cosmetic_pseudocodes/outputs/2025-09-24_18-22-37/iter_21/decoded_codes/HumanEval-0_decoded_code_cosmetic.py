from typing import Sequence

def has_close_elements(sequence_values: Sequence[float], limit_margin: float) -> bool:
    pos_a: int = 0
    length: int = len(sequence_values)
    while pos_a < length:
        coord_a: float = sequence_values[pos_a]
        pos_b: int = 0
        while pos_b < length:
            coord_b: float = sequence_values[pos_b]
            if pos_a == pos_b:
                pass  # skip comparison for the same element
            else:
                delta: float = coord_a - coord_b
                if delta < 0:
                    delta = -delta
                if delta < limit_margin:
                    return True
            pos_b += 1
        pos_a += 1
    return False