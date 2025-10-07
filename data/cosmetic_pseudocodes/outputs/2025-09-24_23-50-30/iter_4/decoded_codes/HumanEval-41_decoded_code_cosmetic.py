from typing import Callable

def car_race_collision(integer_number_of_cars: int) -> int:
    result: int = 0

    def power_accumulate(base: int, exponent: int, accumulator: int) -> None:
        nonlocal result
        if exponent == 0:
            result = accumulator
        else:
            power_accumulate(base, exponent - 1, accumulator * base)

    power_accumulate(integer_number_of_cars, 2, 1)
    return result