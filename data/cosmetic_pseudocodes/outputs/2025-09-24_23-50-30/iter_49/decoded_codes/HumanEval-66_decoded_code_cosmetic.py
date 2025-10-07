from typing import Callable


def digitSum(parameter_alpha: str) -> int:
    def internalSum(index_beta: int, accumulator_gamma: int) -> int:
        if not (index_beta < len(parameter_alpha)):
            return accumulator_gamma
        symbol_delta = parameter_alpha[index_beta]
        increment_epsilon: int
        if 'A' <= symbol_delta <= 'Z':
            increment_epsilon = ord(symbol_delta)
        else:
            increment_epsilon = 0
        return internalSum(index_beta + 1, accumulator_gamma + increment_epsilon)

    return 0 if len(parameter_alpha) == 0 else internalSum(0, 0)