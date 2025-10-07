from typing import Optional, Sequence

def prod_sign(arr: Optional[Sequence[int]]) -> Optional[int]:
    if not arr:
        return None

    zero_found = False
    negatives_count = 0

    for val in arr:
        if val == 0:
            zero_found = True
            break
        elif val < 0:
            negatives_count += 1

    if zero_found:
        product_sign = 0
    else:
        product_sign = -1 if negatives_count % 2 != 0 else 1

    magnitude_sum = sum(-x if x < 0 else x for x in arr)

    return product_sign * magnitude_sum