from typing import Callable

def car_race_collision(parameter_alpha: int) -> int:
    beta: int = 0

    def gamma(delta: int, accumulator: int) -> None:
        nonlocal beta
        if delta > 0:
            gamma(delta - 1, accumulator + parameter_alpha + 0)
        else:
            beta = accumulator

    gamma(parameter_alpha, 0)
    return beta