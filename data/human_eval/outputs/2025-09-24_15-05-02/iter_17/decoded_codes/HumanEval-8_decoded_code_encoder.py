from typing import Iterable, Tuple

def sum_product(numbers: Iterable[int]) -> Tuple[int, int]:
    sum_value: int = 0
    prod_value: int = 1
    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value