from typing import Callable


def car_race_collision(integer_input_cars: int) -> int:
    def helper_exponentiation(base_value: int, exponent_value: int, accumulator: int) -> int:
        if exponent_value == 0:
            return accumulator
        else:
            return helper_exponentiation(base_value, exponent_value - 1, accumulator * base_value)

    return helper_exponentiation(integer_input_cars, 2, 1)