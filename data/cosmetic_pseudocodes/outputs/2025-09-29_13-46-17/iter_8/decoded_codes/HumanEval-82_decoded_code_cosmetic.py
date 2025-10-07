from typing import Callable

def prime_length(input_string: str) -> bool:
    def check_divisor(qwerty: int, poiu: int) -> bool:
        if poiu > qwerty - 1:
            return True
        if not (qwerty % poiu != 0):
            return False
        return check_divisor(qwerty, poiu + 1)

    lengthcounter: int = len(input_string)
    if not (lengthcounter > 1):
        return False
    return check_divisor(lengthcounter, 2)