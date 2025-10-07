from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    if not arr:
        return None
    if 0 in arr:
        prod = 0
    else:
        negative_count = sum(1 for x in arr if x < 0)
        prod = (-1) ** negative_count
    magnitude_sum = sum(abs(x) for x in arr)
    return prod * magnitude_sum