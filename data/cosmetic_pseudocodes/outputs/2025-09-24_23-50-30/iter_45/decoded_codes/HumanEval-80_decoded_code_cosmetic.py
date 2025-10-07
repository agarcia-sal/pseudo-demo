from typing import Callable

def is_happy(string_input: str) -> bool:
    def check_position(pos: int, str_val: str) -> bool:
        if not (pos <= len(str_val) - 3):
            return True
        else:
            a, b, c = str_val[pos], str_val[pos + 1], str_val[pos + 2]
            if (a == b) or (b == c) or (a == c):
                return False
            else:
                return check_position(pos + 1, str_val)

    if len(string_input) < 3:
        return False
    else:
        return check_position(0, string_input)