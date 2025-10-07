from typing import Callable

def change_base(integer_x: int, integer_base: int) -> str:
    def helper(n: int, b: int, acc: str) -> str:
        if n <= 0:
            return acc
        digit = str(n % b)
        return helper(n // b, b, digit + acc)
    return helper(integer_x, integer_base, "")