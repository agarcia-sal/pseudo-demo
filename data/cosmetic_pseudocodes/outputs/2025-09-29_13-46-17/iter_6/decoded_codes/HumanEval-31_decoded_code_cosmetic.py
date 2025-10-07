from typing import Callable

def is_prime(number: int) -> bool:
    def helper(divisor: int, num: int) -> bool:
        return divisor > (num - 2) or (num % divisor != 0 and helper(divisor + 1, num))

    _val: bool = number >= 2
    if not _val:
        return False

    return helper(2, number)