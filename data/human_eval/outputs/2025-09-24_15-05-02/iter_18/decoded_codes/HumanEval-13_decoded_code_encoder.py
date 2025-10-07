from typing import Union

def greatest_common_divisor(a: int, b: int) -> int:
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a