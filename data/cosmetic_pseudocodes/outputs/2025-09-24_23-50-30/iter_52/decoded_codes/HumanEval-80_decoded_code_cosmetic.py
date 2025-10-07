from typing import Callable

def is_happy(alphanumeric_value: str) -> bool:
    def loop_checker(counter: int) -> bool:
        if counter > len(alphanumeric_value) - 3:
            return True
        if (alphanumeric_value[counter] == alphanumeric_value[counter + 1] or
            alphanumeric_value[counter + 1] == alphanumeric_value[counter + 2] or
            alphanumeric_value[counter] == alphanumeric_value[counter + 2]):
            return False
        return loop_checker(counter + 1)

    if len(alphanumeric_value) < 3:
        return False
    return loop_checker(0)