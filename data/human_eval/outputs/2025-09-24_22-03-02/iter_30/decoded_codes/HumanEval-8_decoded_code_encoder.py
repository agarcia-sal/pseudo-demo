from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum_value = 0
    prod_value = 1
    index = 0
    length = len(numbers)
    while index < length:
        n = numbers[index]
        sum_value += n
        prod_value *= n
        index += 1
    return (sum_value, prod_value)