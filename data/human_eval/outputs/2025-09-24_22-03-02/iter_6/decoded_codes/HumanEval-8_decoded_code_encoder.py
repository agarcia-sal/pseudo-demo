from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum_value = 0
    prod_value = 1
    for number in numbers:
        sum_value += number
        prod_value *= number
    return sum_value, prod_value