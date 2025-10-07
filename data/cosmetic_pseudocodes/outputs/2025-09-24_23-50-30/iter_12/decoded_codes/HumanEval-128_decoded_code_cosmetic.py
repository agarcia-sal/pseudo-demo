from typing import List, Optional


def prod_sign(input_list: List[int]) -> Optional[int]:
    if not input_list:
        return None

    has_zero_flag: bool = False
    negative_count: int = 0

    for element in input_list:
        if element == 0:
            has_zero_flag = True
            break

    if has_zero_flag:
        product_sign: int = 0
    else:
        for element in input_list:
            if element < 0:
                negative_count += 1
        product_sign = 1
        while negative_count > 0:
            product_sign = -product_sign
            negative_count -= 1

    magnitude_sum: int = sum(abs(element) for element in input_list)

    return product_sign * magnitude_sum