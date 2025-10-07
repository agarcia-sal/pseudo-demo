from typing import Union

def greatest_common_divisor(a: int, b: int) -> int:
    while b != 0:
        temporary: int = b
        b = a % b
        a = temporary
    return a