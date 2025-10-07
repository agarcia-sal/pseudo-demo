from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    if not arr:
        return None
    if 0 in arr:
        prod = 0
    else:
        negative_count = sum(1 for element in arr if element < 0)
        prod = (-1) ** negative_count
    total_magnitude = sum(abs(element) for element in arr)
    return prod * total_magnitude