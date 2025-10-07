from typing import Callable

def count_upper(string_input: str) -> int:
    accumulator: int = 0

    def recurse(position: int) -> int:
        nonlocal accumulator
        if position >= len(string_input):
            return accumulator
        if string_input[position] in {"A", "E", "I", "O", "U"}:
            accumulator += 1
        return recurse(position + 2)

    return recurse(0)