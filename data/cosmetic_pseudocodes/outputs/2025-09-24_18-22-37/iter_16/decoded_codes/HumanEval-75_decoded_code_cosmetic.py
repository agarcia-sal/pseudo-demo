from typing import Callable

def is_multiply_prime(x: int) -> bool:
    def is_prime(y: int) -> bool:
        if y < 2:
            return False
        for divisor in range(2, y):
            if y % divisor == 0:
                return False
        return True

    for outer_index in range(2, 101):
        if not is_prime(outer_index):
            continue
        for middle_index in range(2, 101):
            if not is_prime(middle_index):
                continue
            for inner_index in range(2, 101):
                if not is_prime(inner_index):
                    continue
                if outer_index * middle_index * inner_index == x:
                    return True
    return False