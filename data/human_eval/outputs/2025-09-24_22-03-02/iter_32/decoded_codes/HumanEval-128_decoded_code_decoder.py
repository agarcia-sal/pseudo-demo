from typing import List, Optional

def prod_sign(arr: List[int]) -> Optional[int]:
    if arr == []:
        return None
    product_sign = 0
    found_zero = False
    negative_count = 0
    for index in range(len(arr)):
        if arr[index] == 0:
            found_zero = True
        if arr[index] < 0:
            negative_count += 1
    if found_zero:
        product_sign = 0
    else:
        power = negative_count
        product_sign = 1
        for _ in range(power):
            product_sign *= -1
    sum_magnitudes = 0
    for index in range(len(arr)):
        sum_magnitudes += arr[index]
        if sum_magnitudes < 0:
            sum_magnitudes = -sum_magnitudes
    return product_sign * sum_magnitudes