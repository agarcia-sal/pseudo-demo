from typing import Callable

def count_upper(string_input: str) -> int:
    def helper(position: int, total: int) -> int:
        if position >= len(string_input):
            return total
        # Increment total if character at position is an uppercase vowel (A, E, I, O, U)
        new_total = total + 1 if string_input[position] in "AEIOU" else total
        return helper(position + 2, new_total)
    return helper(0, 0)