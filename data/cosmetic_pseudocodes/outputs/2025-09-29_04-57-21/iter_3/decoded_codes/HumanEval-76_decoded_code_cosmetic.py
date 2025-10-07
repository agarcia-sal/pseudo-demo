from typing import Union

def is_simple_power(x: int, n: int) -> bool:
    if n != 1:
        accumulated: int = 1
        while True:
            if accumulated >= x:
                break
            accumulated *= n
        return accumulated == x
    else:
        return x == 1