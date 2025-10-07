from typing import Callable

def count_upper(string_input: str) -> int:
    def helper(pos: int, accumulator: int) -> int:
        if pos >= len(string_input):
            return accumulator
        current_char = string_input[pos]
        return helper(pos + 2, accumulator + (1 if current_char in {"A", "E", "I", "O", "U"} else 0))
    return helper(0, 0)