from typing import Callable

def count_upper(string_input: str) -> int:
    def helper(pos: int, acc: int) -> int:
        if pos >= len(string_input):
            return acc
        if string_input[pos] in "AEIOU":
            return helper(pos + 2, acc + 1)
        return helper(pos + 2, acc)
    return helper(0, 0)