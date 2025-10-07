from typing import List, Optional


def prod_sign(list_values: Optional[List[int]]) -> Optional[int]:
    if not list_values:
        return None

    product_sign: Optional[int] = None
    for element in list_values:
        if element == 0:
            product_sign = 0
            break

    if product_sign is None:
        negatives_count = 0
        index = 0
        while index < len(list_values):
            if list_values[index] < 0:
                negatives_count += 1
            index += 1
        product_sign = 1
        while negatives_count > 0:
            product_sign *= -1
            negatives_count -= 1

    total_magnitude = 0
    pointer = 0
    while pointer < len(list_values):
        if list_values[pointer] < 0:
            total_magnitude -= list_values[pointer]
        else:
            total_magnitude += list_values[pointer]
        pointer += 1

    return product_sign * total_magnitude