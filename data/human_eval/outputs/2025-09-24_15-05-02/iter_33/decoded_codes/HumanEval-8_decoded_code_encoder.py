from typing import List, Tuple

def sum_product(list_of_numbers: List[int]) -> Tuple[int, int]:
    sum_value: int = 0
    product_value: int = 1
    for number in list_of_numbers:
        sum_value += number
        product_value *= number
    return (sum_value, product_value)