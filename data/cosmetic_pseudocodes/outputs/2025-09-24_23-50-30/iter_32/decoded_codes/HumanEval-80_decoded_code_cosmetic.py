from typing import Callable

def is_happy(string_input: str) -> bool:
    def check_pair(position: int, bool_flag: bool) -> bool:
        if position > len(string_input) - 3:
            return bool_flag
        x, y, z = string_input[position], string_input[position + 1], string_input[position + 2]
        if not (x != y and y != z and x != z):
            return False
        return check_pair(position + 1, bool_flag)

    if len(string_input) < 3:
        return False
    return check_pair(0, True)