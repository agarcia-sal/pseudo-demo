from typing import List, Tuple

def sum_product(list_of_numbers: List[int]) -> Tuple[int, int]:
    sum_value = 0
    prod_value = 1
    for n in list_of_numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value