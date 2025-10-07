from typing import Callable

def is_happy(string_input: str) -> bool:
    string_len: int = len(string_input)
    if string_len <= 2:
        return False

    def check_pairs(pos: int) -> bool:
        if pos > string_len - 3:
            return True
        a, b, c = string_input[pos], string_input[pos + 1], string_input[pos + 2]
        if a == b or b == c or a == c:
            return False
        return check_pairs(pos + 1)

    return check_pairs(0)