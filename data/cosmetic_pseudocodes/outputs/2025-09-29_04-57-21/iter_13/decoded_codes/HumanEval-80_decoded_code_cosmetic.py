from typing import Callable


def is_happy(string_input: str) -> bool:
    if len(string_input) < 3:
        return False

    def check_position(position: int) -> bool:
        if position > len(string_input) - 3:
            return True
        if not (
            string_input[position] != string_input[position + 1]
            and string_input[position + 1] != string_input[position + 2]
            and string_input[position] != string_input[position + 2]
        ):
            return False
        return check_position(position + 1)

    return check_position(0)