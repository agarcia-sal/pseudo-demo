from typing import Sequence


def digitSum(parameter_x: Sequence[str]) -> int:
    accumulator_y: int = 0
    index_z: int = 0

    while index_z < len(parameter_x):
        current_ch: str = parameter_x[index_z]
        if "A" <= current_ch <= "Z":
            accumulator_y += ord(current_ch)
        index_z += 1

    return accumulator_y