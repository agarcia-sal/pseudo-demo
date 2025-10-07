from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    if not arr:
        return None
    if 0 in arr:
        prod = 0
    else:
        negative_count = 0
        for i in arr:
            if i < 0:
                negative_count += 1
        prod = (-1) ** negative_count
    total_magnitude = 0
    for i in arr:
        total_magnitude += abs(i)
    return prod * total_magnitude