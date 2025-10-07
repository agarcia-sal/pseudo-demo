from typing import Union

def greatest_common_divisor(x: int, y: int) -> int:
    while True:
        if y == 0:
            break
        temp = y
        y = x - (x // y) * y
        x = temp
    return x