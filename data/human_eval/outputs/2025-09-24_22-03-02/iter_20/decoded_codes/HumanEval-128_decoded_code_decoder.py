from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    if arr == []:
        return None

    zero_found = False
    index = 0
    while index < len(arr):
        if arr[index] == 0:
            zero_found = True
            break
        index += 1

    if zero_found:
        prod = 0
    else:
        negative_count = 0
        index = 0
        while index < len(arr):
            if arr[index] < 0:
                negative_count += 1
            index += 1

        power = negative_count
        prod = 1
        power_counter = 0
        while power_counter < power:
            prod *= -1
            power_counter += 1

    sum_magnitudes = 0
    index = 0
    while index < len(arr):
        element = arr[index]
        if element < 0:
            absolute_value = element * -1
        else:
            absolute_value = element
        sum_magnitudes += absolute_value
        index += 1

    result = prod * sum_magnitudes
    return result