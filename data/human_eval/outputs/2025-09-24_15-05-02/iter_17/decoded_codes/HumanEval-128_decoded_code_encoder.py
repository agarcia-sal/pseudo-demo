from typing import List, Optional, Union

def prod_signs(arr: List[int]) -> Optional[int]:
    if not arr:
        return None
    if 0 in arr:
        prod: int = 0
    else:
        negative_count: int = sum(1 for element in arr if element < 0)
        prod = (-1) ** negative_count
    magnitude_sum: int = sum(abs(element) for element in arr)
    return prod * magnitude_sum