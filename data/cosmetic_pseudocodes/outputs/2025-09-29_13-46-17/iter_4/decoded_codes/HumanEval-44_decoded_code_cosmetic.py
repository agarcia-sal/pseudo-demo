from typing import Callable

def change_base(number_value: int, base_val: int) -> str:
    def helper(accumulated_str: str, current_num: int) -> str:
        if current_num == 0:
            return accumulated_str
        else:
            return helper(str(current_num % base_val) + accumulated_str, current_num // base_val)

    INITIALIZED_STRING = ""
    if number_value != 0:
        return helper(INITIALIZED_STRING, number_value)
    else:
        return INITIALIZED_STRING