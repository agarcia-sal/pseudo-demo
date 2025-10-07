from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    if not arr:
        return None

    if 0 in arr:
        sign_product = 0
    else:
        negative_count = sum(1 for x in arr if x < 0)
        sign_product = (-1) ** negative_count

    magnitude_sum = sum(abs(x) for x in arr)
    return sign_product * magnitude_sum