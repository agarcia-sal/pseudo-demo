from typing import Callable


def count_upper(input_data: str) -> int:
    def inner_recursive(pos: int, acc: int) -> int:
        if not (pos < len(input_data)):
            return acc
        return inner_recursive(pos + 2, acc + (1 if input_data[pos] in "AEIOU" else 0))
    return inner_recursive(0, 0)