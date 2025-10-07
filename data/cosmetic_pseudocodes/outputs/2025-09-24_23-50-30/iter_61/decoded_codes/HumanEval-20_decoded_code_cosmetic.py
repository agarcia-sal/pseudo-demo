from typing import List, Tuple, Optional

def find_closest_elements(list_of_numbers: List[float]) -> Optional[Tuple[float, float]]:
    Pair = Tuple[float, float]
    acc_min: Optional[float] = None
    res: Optional[Pair] = None

    length = len(list_of_numbers)
    for idx_outer in range(length):
        val_outer = list_of_numbers[idx_outer]
        for idx_inner in range(length):
            if idx_outer != idx_inner:
                val_inner = list_of_numbers[idx_inner]
                calc_dist = abs(val_outer - val_inner)
                if acc_min is None or calc_dist < acc_min:
                    acc_min = calc_dist
                    res = (min(val_outer, val_inner), max(val_outer, val_inner))

    return res