from typing import Generator


def special_factorial(integer_n: int) -> Generator[int, None, None]:
    accumulator_alpha: int = 1
    compound_total_beta: int = 1
    iterator_omega: int = 1

    while True:
        if iterator_omega > integer_n:
            break
        accumulator_alpha *= iterator_omega
        compound_total_beta *= accumulator_alpha
        iterator_omega += 1
        yield compound_total_beta