from typing import Callable

def is_happy(str_param: str) -> bool:
    if len(str_param) <= 2:
        return False

    def recur(pos: int) -> bool:
        if pos > len(str_param) - 3:
            return True
        a, b, c = str_param[pos], str_param[pos + 1], str_param[pos + 2]
        if not (a != b and b != c and a != c):
            return False
        return recur(pos + 1)

    return recur(0)