from typing import Callable


def is_happy(string_input: str) -> bool:
    if len(string_input) < 3:
        return False

    def check_sequence(pos: int, limit: int) -> bool:
        if pos > limit:
            return True
        if string_input[pos] == string_input[pos + 1]:
            return False
        if string_input[pos + 1] == string_input[pos + 2]:
            return False
        if string_input[pos] == string_input[pos + 2]:
            return False
        return check_sequence(pos + 1, limit)

    return check_sequence(0, len(string_input) - 3)