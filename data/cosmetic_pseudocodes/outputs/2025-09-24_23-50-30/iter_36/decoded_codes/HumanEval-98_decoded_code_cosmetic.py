from typing import Callable

def count_upper(string_input: str) -> int:
    def loop_accumulate(position: int, accumulator: int) -> int:
        if position >= len(string_input):
            return accumulator
        return loop_accumulate(position + 2, accumulator + (1 if string_input[position] in "AEIOU" else 0))
    return loop_accumulate(0, 0)