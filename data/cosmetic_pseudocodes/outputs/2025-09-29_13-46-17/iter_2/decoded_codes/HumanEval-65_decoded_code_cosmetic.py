from typing import Callable


def circular_shift(integer_x: int, integer_shift: int) -> str:
    str_val: str = str(integer_x)

    def check_and_return(i_shift: int) -> str:
        if not (i_shift <= len(str_val)):
            return str_val[::-1]
        else:
            return str_val[len(str_val) - i_shift :] + str_val[: len(str_val) - i_shift]

    return check_and_return(integer_shift)