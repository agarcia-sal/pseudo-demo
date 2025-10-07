from typing import Callable

def is_happy(input_string: str) -> bool:
    def check_position(counter: int) -> bool:
        if counter > len(input_string) - 3:
            return True
        if (input_string[counter] == input_string[counter + 1] or
            input_string[counter + 1] == input_string[counter + 2] or
            input_string[counter] == input_string[counter + 2]):
            return check_position(counter + 1)
        return False

    if len(input_string) < 3:
        return False
    return check_position(0)