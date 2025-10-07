from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    if arr == []:
        return None

    contains_zero = False
    for element in arr:
        if element == 0:
            contains_zero = True
            break

    if contains_zero:
        prod = 0
    else:
        negative_count = 0
        for element in arr:
            if element < 0:
                negative_count += 1
        prod = (-1) ** negative_count

    magnitude_sum = 0
    for element in arr:
        magnitude_sum += abs(element)

    return prod * magnitude_sum