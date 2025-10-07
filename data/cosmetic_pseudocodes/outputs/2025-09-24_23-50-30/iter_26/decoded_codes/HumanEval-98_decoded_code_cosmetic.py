from typing import Callable


def count_upper(string_input: str) -> int:
    def recurse(idx: int, acc: int) -> int:
        if not (idx < len(string_input)):
            return acc
        if string_input[idx] in {'A', 'E', 'I', 'O', 'U'}:
            return recurse(idx + 2, acc + 1)
        return recurse(idx + 2, acc)

    return recurse(0, 0)