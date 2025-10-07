from typing import NoReturn

def special_factorial(count_of_numbers: int) -> int:
    factor_product: int = 1
    special_result: int = 1
    counter: int = 1
    while counter <= count_of_numbers:
        factor_product *= counter
        special_result *= factor_product
        counter += 1
    return special_result