from typing import Callable


def car_race_collision(integer_number_of_cars: int) -> int:
    def compute_square(value: int) -> int:
        if value == 0:
            return 0
        return value * value

    return compute_square(integer_number_of_cars)