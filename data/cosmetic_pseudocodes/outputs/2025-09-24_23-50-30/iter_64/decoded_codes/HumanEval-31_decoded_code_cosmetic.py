from typing import Callable

def is_prime(input_a: int) -> bool:
    def helper_b(counter_c: int) -> bool:
        if counter_c > input_a - 2:
            return True
        if input_a % counter_c == 0:
            return False
        return helper_b(counter_c + 1)

    if input_a <= 1:
        return False
    return helper_b(2)