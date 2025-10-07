from typing import Sequence


def same_chars(param_x: Sequence[str], param_y: Sequence[str]) -> bool:
    tempSetA = set(param_x)
    tempSetB = set(param_y)
    return tempSetA == tempSetB