from typing import Callable

def count_upper(string_input: str) -> int:
    def helper(position: int, accumulator: int) -> int:
        if position >= len(string_input):
            return accumulator
        new_accumulator = accumulator + (1 if string_input[position] in {"A", "E", "I", "O", "U"} else 0)
        return helper(position + 2, new_accumulator)

    return helper(0, 0)