from typing import Callable


def count_upper(string_input: str) -> int:
    def recurse(pos: int, acc: int) -> int:
        if pos >= len(string_input):
            return acc
        if string_input[pos] in {'A', 'E', 'I', 'O', 'U'}:
            return recurse(pos + 2, acc + 1)
        return recurse(pos + 2, acc)

    return recurse(0, 0)