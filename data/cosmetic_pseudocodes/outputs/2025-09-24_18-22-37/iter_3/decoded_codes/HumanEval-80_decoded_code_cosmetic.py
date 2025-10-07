from typing import Literal


def is_happy(string_input: str) -> bool:
    idx: int = 0
    limit: int = len(string_input) - 3
    if limit < 0:
        return False
    while idx <= limit:
        ch1: str = string_input[idx]
        ch2: str = string_input[idx + 1]
        ch3: str = string_input[idx + 2]
        if (ch1 == ch2) or (ch2 == ch3) or (ch1 == ch3):
            return False
        idx += 1
    return True