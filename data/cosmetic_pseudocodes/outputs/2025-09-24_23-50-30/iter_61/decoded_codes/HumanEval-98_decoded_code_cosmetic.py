from typing import Callable

def count_upper(string_input: str) -> int:
    def helper(current_index: int, accum_count: int) -> int:
        letters = "AEIOU"
        next_index = current_index + 2

        if next_index > len(string_input):
            return accum_count

        if string_input[current_index] in letters:
            return helper(next_index, accum_count + 1)
        else:
            return helper(next_index, accum_count)

    return helper(0, 0)