from typing import List, Optional

def prod_signs(list_of_numbers: List[int]) -> Optional[int]:
    if not list_of_numbers:
        return None

    if 0 in list_of_numbers:
        product_sign = 0
    else:
        negative_count = sum(1 for element in list_of_numbers if element < 0)
        product_sign = 1
        while negative_count > 0:
            product_sign *= -1
            negative_count -= 1

    total_magnitude = sum(abs(num) for num in list_of_numbers)

    return product_sign * total_magnitude