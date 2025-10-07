from typing import Optional, Sequence, Tuple

def find_closest_elements(input_sequence: Sequence[int]) -> Optional[Tuple[int, int]]:
    result_pair: Optional[Tuple[int, int]] = None
    min_gap: Optional[int] = None

    for idx_a, val_a in enumerate(input_sequence):
        for idx_b, val_b in enumerate(input_sequence):
            if idx_a != idx_b:
                current_gap = abs(val_a - val_b)
                if min_gap is None or current_gap < min_gap:
                    min_gap = current_gap
                    low, high = (val_a, val_b) if val_a <= val_b else (val_b, val_a)
                    result_pair = (low, high)

    return result_pair