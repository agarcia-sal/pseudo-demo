from typing import List, Optional


def prod_signs(list_of_vals: List[int]) -> Optional[int]:
    if not list_of_vals:
        return None
    if 0 in list_of_vals:
        signal_val: int = 0
    else:
        neg_count: int = sum(val < 0 for val in list_of_vals)
        signal_val = (-1) ** neg_count
    total_mag: int = sum(abs(val) for val in list_of_vals)
    return signal_val * total_mag