from typing import Callable

def how_many_times(parameter_alpha: str, parameter_beta: str) -> int:
    def traverse(position_gamma: int, accumulator_delta: int) -> int:
        if position_gamma > len(parameter_alpha) - len(parameter_beta):
            return accumulator_delta
        return traverse(
            position_gamma + 1,
            accumulator_delta + (1 if parameter_alpha[position_gamma:position_gamma + len(parameter_beta)] == parameter_beta else 0)
        )
    return traverse(0, 0)