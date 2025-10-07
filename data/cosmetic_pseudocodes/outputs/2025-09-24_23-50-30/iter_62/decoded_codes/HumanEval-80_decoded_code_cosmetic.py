from typing import Callable

def is_happy(text_value: str) -> bool:
    def check_position(pos_val: int) -> bool:
        if pos_val > len(text_value) - 3:
            return True
        if (text_value[pos_val] == text_value[pos_val + 1] or
            text_value[pos_val + 1] == text_value[pos_val + 2] or
            text_value[pos_val] == text_value[pos_val + 2]):
            return False
        return check_position(pos_val + 1)

    if len(text_value) < 3:
        return False

    return check_position(0)