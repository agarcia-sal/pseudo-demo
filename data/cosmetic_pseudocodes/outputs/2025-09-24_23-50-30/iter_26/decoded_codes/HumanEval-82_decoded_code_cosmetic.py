from typing import Callable

def prime_length(input_string: str) -> bool:
    size_val: int = len(input_string)
    if size_val == 0 or size_val == 1:
        return False

    def divisor_check(counter: int) -> bool:
        if counter >= size_val:
            return True
        if size_val % counter == 0:
            return False
        return divisor_check(counter + 1)

    return divisor_check(2)