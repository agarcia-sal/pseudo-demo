from typing import Callable

def car_race_collision(countOfCars: int) -> int:
    result: int = 1

    def power(base: int, exponent: int, accumulator: int) -> None:
        nonlocal result
        if exponent != 0:
            power(base, exponent - 1, accumulator * base)
        else:
            result = accumulator

    power(countOfCars, 2, 1)
    return result