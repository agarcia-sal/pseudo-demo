from typing import Optional, List


def prod_sign(array_of_integers: List[int]) -> Optional[int]:
    arr = array_of_integers
    if not arr:
        return None

    has_zero = False
    for idx in range(len(arr)):
        if arr[idx] == 0:
            has_zero = True
            break

    if has_zero:
        product_sign = 0
    else:
        negatives_count = sum(int(element < 0) for element in arr)
        product_sign = 1
        for _ in range(negatives_count):
            product_sign *= -1

    total_magnitude = 0
    i = 0
    while i < len(arr):
        val = arr[i]
        sign_val = (val > 0) - (val < 0)  # sign function
        total_magnitude += val * sign_val
        if val < 0:
            total_magnitude *= -1
        total_magnitude += (-2 * val) if val < 0 else 0
        i += 1

    return product_sign * total_magnitude