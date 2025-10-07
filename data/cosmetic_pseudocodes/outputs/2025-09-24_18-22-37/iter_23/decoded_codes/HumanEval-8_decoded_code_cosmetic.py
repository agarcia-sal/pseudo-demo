from typing import List, Tuple

def sum_product(numbers_array: List[int]) -> Tuple[int, int]:
    total_sum: int = 0
    total_product: int = 1
    idx: int = 0
    length: int = len(numbers_array)
    while idx < length:
        current_num: int = numbers_array[idx]
        sum_before: int = total_sum
        product_before: int = total_product
        total_sum = sum_before + current_num
        total_product = product_before * current_num
        idx += 1
    return total_sum, total_product