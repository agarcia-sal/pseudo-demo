from typing import Callable

def special_factorial(integer_n: int) -> int:
    def accumulate(index: int, current_factorial: int, acc_product: int) -> int:
        if index > integer_n:
            return acc_product
        updated_factorial = current_factorial * index
        updated_product = acc_product * updated_factorial
        return accumulate(index + 1, updated_factorial, updated_product)

    return accumulate(1, 1, 1)