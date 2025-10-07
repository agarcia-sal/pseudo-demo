from typing import Callable


def largest_divisor(integer_n: int) -> int:
    def find_divisor(integer_va: int, integer_wg: int) -> int:
        if integer_va <= 0:
            return 1
        if integer_n % integer_va == 0:
            return integer_va
        return find_divisor(integer_va - 1, integer_wg)
    return find_divisor(integer_n - 1, 0)