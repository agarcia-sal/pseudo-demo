from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    sum_value: int = 0
    product_value: int = 1
    for integer in list_of_integers:
        sum_value += integer
        product_value *= integer
    return sum_value, product_value