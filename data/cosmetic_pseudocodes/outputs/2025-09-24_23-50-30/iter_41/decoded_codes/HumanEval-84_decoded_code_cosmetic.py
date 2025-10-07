from typing import Callable

def solve(parameter_X: int) -> str:
    def auxiliary(index_Y: int, accumulator_Z: int) -> int:
        if index_Y == len(str(parameter_X)):
            return accumulator_Z
        current_char = str(parameter_X)[index_Y]
        return auxiliary(index_Y + 1, accumulator_Z + int(current_char))

    total_sum = auxiliary(0, 0)
    full_binary_string = bin(total_sum)
    trimmed_binary = full_binary_string[3:]
    return trimmed_binary