from typing import Callable

def count_upper(string_input: str) -> int:
    def helper(position: int, accumulator: int) -> int:
        if position >= len(string_input):
            return accumulator
        return helper(position + 2, accumulator + (1 if string_input[position] in "AEIOU" else 0))
    return helper(0, 0)