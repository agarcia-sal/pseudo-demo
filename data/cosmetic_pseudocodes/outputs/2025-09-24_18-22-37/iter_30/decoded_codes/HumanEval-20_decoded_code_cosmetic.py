from typing import List, Optional, Tuple

def find_closest_elements(numbers_list: List[int]) -> Optional[Tuple[int, int]]:
    pair_with_min_gap: Optional[Tuple[int, int]] = None
    smallest_gap: Optional[int] = None

    idx_a = 0
    while idx_a < len(numbers_list):
        val_a = numbers_list[idx_a]
        idx_b = 0

        while idx_b < len(numbers_list):
            val_b = numbers_list[idx_b]
            if idx_a != idx_b:
                gap_calc = abs(val_a - val_b)
                if smallest_gap is None or gap_calc < smallest_gap:
                    smallest_gap = gap_calc
                    pair_with_min_gap = (val_a, val_b) if val_a < val_b else (val_b, val_a)
            idx_b += 1
        idx_a += 1

    return pair_with_min_gap