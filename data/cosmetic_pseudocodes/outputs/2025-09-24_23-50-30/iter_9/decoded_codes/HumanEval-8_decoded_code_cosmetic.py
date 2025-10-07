from typing import Iterable, Tuple

def sum_product(values: Iterable[int]) -> Tuple[int, int]:
    s_sum: int = 0
    s_prod: int = 1
    index: int = 0
    values_list = list(values)  # ensure multiple passes and length calculation
    while index < len(values_list):
        num = values_list[index]
        s_sum += num
        s_prod *= num
        index += 1
    return s_sum, s_prod