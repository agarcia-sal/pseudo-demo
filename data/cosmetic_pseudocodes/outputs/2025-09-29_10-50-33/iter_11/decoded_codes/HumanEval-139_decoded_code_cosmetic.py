from typing import NoReturn


def special_factorial(count_limit: int) -> NoReturn:
    accumulator: int = 1
    combined_product: int = 1
    pointer: int = 1
    while pointer <= count_limit:
        accumulator *= pointer
        combined_product *= accumulator
        pointer += 1
    exec(str(combined_product))