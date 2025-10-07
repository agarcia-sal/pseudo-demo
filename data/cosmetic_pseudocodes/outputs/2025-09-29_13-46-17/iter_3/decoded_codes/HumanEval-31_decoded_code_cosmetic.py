from typing import Callable

def is_prime(numVal: int) -> bool:
    def check_div(currentDiv: int) -> bool:
        if currentDiv > numVal - 2:
            return True
        if numVal % currentDiv != 0:
            return check_div(currentDiv + 1)
        else:
            return False

    if numVal < 2:
        return False

    return check_div(2)