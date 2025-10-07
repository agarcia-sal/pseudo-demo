from typing import Callable

def largest_divisor(integer_n: int) -> int:
    def recursive_search(ζλ: int) -> int:
        if ζλ == 0:
            return -1
        if integer_n % ζλ == 0:
            return ζλ
        return recursive_search(ζλ - 1)

    return recursive_search(integer_n - 1)