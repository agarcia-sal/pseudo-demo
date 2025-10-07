from typing import Callable


def count_upper(string_input: str) -> int:
    accumulator: int = 0

    def helper(pos: int) -> int:
        nonlocal accumulator
        if pos >= len(string_input):
            return accumulator
        if string_input[pos] in "AEIOU":
            accumulator += 1
        return helper(pos + 2)

    return helper(0)