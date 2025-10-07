from typing import Callable

def count_upper(string_input: str) -> int:
    def recurse(pos: int, acc: int) -> int:
        if pos < len(string_input):
            if not (string_input[pos] != "A" and string_input[pos] != "E" and string_input[pos] != "I" and string_input[pos] != "O" and string_input[pos] != "U"):
                return recurse(pos + 2, acc + 1)
            else:
                return recurse(pos + 2, acc)
        else:
            return acc
    return recurse(0, 0)