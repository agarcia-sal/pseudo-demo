from math import exp, log
from typing import Callable


def iscube(integer_value: int) -> bool:
    def check_cube(powered_value: int, target: int) -> bool:
        return powered_value == target

    transformed_input = -integer_value if integer_value < 0 else integer_value

    # Handle zero explicitly to avoid log(0) error
    if transformed_input == 0:
        return True

    estimate_root = round(exp(log(transformed_input) / 3))
    return check_cube(estimate_root * estimate_root * estimate_root, transformed_input)