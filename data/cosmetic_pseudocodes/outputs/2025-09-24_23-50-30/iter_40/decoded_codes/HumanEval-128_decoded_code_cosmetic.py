from typing import List, Optional


def prod_signs(list_of_values: List[int]) -> Optional[int]:
    if not list_of_values:
        return None
    if any(x == 0 for x in list_of_values):
        v = 0
    else:
        u = sum(1 for e in list_of_values if e < 0)
        v = (-1) ** u
    w = sum(abs(y) for y in list_of_values)
    return v * w