from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    if len(arr) == 0:
        return None
    zero_found = any(x == 0 for x in arr)
    if zero_found:
        prod = 0
    else:
        negative_count = sum(1 for x in arr if x < 0)
        prod = -1 if negative_count % 2 else 1
    total_sum = sum(abs(x) for x in arr)
    return prod * total_sum