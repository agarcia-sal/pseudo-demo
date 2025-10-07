from typing import Callable

def special_factorial(integer_n: int) -> int:
    cumulative_product: int = 1
    aggregate_factorial: int = 1

    def helper_loop(index: int) -> None:
        nonlocal cumulative_product, aggregate_factorial
        if index <= integer_n:
            cumulative_product *= index
            aggregate_factorial *= cumulative_product
            helper_loop(index + 1)

    helper_loop(1)
    return aggregate_factorial