from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    if len(arr) == 0:
        return None
    contains_zero = any(element == 0 for element in arr)
    if contains_zero:
        prod = 0
    else:
        negative_count = sum(1 for element in arr if element < 0)
        prod = -1 if negative_count % 2 else 1
    magnitude_sum = sum(abs(element) for element in arr)
    return prod * magnitude_sum