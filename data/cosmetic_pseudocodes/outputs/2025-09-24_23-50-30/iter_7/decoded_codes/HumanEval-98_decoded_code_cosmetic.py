from typing import Callable

def count_upper(string_input: str) -> int:
    def helper(position: int, accumulator: int) -> int:
        if position >= len(string_input):
            return accumulator
        if string_input[position] in {'A', 'E', 'I', 'O', 'U'}:
            return helper(position + 2, accumulator + 1)
        return helper(position + 2, accumulator)
    return helper(0, 0)