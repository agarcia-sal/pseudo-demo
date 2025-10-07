from typing import List, Tuple

def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    if not list_of_integers:
        # sum is 0 and product is 1 by definition for empty list
        return 0, 1
    sum_value: int = 0
    prod_value: int = 1
    for integer in list_of_integers:
        sum_value += integer
        prod_value *= integer
    return sum_value, prod_value