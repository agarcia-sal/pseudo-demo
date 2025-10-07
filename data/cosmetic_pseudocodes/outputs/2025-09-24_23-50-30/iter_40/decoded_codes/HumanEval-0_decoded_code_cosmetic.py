from typing import Sequence

def has_close_elements(sequence: Sequence[int], limit: int) -> bool:
    for pos_a, val_a in enumerate(sequence):
        for pos_b, val_b in enumerate(sequence):
            if pos_a != pos_b:
                dist = abs(val_a - val_b)
                if dist < limit:
                    return True
    return False