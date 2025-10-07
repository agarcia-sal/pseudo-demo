from typing import Callable


def is_happy(string_input: str) -> bool:
    length: int = len(string_input)

    def helper(idx: int) -> bool:
        if idx >= length - 3:
            return True
        a: str = string_input[idx]
        b: str = string_input[idx + 1]
        c: str = string_input[idx + 2]
        all_different: bool = (a != b) and (b != c) and (a != c)
        if all_different:
            return False
        return helper(idx + 1)

    if length < 3:
        return False
    return helper(0)