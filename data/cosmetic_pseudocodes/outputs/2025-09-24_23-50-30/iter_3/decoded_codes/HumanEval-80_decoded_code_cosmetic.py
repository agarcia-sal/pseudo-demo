from typing import Literal


def is_happy(string_input: str) -> bool:
    if len(string_input) < 3:
        return False
    pos = 0
    while pos <= len(string_input) - 3:
        if (
            string_input[pos] == string_input[pos + 1]
            or string_input[pos + 1] == string_input[pos + 2]
            or string_input[pos] == string_input[pos + 2]
        ):
            return False
        pos += 1
    return True