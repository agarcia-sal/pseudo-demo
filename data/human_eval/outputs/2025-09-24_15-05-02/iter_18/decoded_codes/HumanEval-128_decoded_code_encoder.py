from typing import Optional, Sequence

def prod_signs(arr: Sequence[int]) -> Optional[int]:
    if not arr:
        return None
    if 0 in arr:
        prod = 0
    else:
        negative_count = sum(1 for x in arr if x < 0)
        prod = (-1) ** negative_count
    total_abs_sum = sum(abs(x) for x in arr)
    return prod * total_abs_sum