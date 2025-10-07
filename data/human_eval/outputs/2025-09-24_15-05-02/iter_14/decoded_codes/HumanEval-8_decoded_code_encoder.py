from typing import List, Tuple

def sum_product(list_of_numbers: List[int]) -> Tuple[int, int]:
    sum_value = 0
    prod_value = 1
    for number in list_of_numbers:
        sum_value += number
        prod_value *= number
    return (sum_value, prod_value)