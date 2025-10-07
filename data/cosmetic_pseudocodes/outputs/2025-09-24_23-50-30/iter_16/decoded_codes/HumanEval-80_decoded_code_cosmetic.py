from typing import Callable


def is_happy(string_input: str) -> bool:
    def check_position(pos: int, limit: int, text: str) -> bool:
        if pos > limit:
            return True
        if not (text[pos] != text[pos + 1] and text[pos + 1] != text[pos + 2]):
            # If all three characters are equal, return False
            return False
        if (
            text[pos] == text[pos + 1]
            or text[pos + 1] == text[pos + 2]
            or text[pos] == text[pos + 2]
        ):
            return False
        return check_position(pos + 1, limit, text)

    if len(string_input) < 3:
        return False

    return check_position(0, len(string_input) - 3, string_input)