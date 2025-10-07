from typing import Callable

def change_base(integer_x: int, integer_base: int) -> str:
    def internal_convert(n: int, acc: str) -> str:
        if n <= 0:
            return acc
        else:
            return internal_convert(n // integer_base, str(n % integer_base) + acc)
    return internal_convert(integer_x, "")