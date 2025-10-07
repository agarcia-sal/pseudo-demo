from typing import Callable


def car_race_collision(integer_number_of_cars: int) -> int:
    def _exponential_counter(x_param: int, power_depth: int, acc_rescuer: int) -> int:
        if power_depth == 0:
            return acc_rescuer
        return _exponential_counter(x_param, power_depth - 1, acc_rescuer * x_param)

    return _exponential_counter(integer_number_of_cars, 2, 1)