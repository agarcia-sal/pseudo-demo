from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    idx: int = len(list_of_integers) - 1
    product_value: int = 1
    sum_value: int = 0
    while idx >= 0:
        product_value *= list_of_integers[idx]
        sum_value += list_of_integers[idx]
        idx -= 1
    return sum_value, product_value