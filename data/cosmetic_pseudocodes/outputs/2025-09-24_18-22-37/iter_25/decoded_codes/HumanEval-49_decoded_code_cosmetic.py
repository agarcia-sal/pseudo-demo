from typing import Optional

def modp(integer_n: int, integer_p: int) -> int:
    accumulator: int = 1
    counter: int = 0
    while counter < integer_n:
        temp: int = accumulator * 2
        accumulator = temp - ((temp // integer_p) * integer_p)
        counter += 1
    return accumulator