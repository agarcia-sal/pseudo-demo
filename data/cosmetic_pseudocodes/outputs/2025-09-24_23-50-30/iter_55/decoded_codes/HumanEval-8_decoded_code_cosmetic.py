from typing import List, Tuple

def sum_product(arr_numbers: List[int]) -> Tuple[int, int]:
    idx: int = 0
    acc_sum: int = 0
    acc_prod: int = 1
    while idx < len(arr_numbers):
        acc_sum += arr_numbers[idx]
        acc_prod *= arr_numbers[idx]
        idx += 1
    return acc_sum, acc_prod