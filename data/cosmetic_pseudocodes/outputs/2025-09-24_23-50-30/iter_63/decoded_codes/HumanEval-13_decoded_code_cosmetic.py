from typing import Union

def greatest_common_divisor(p: int, q: int) -> int:
    if q == 0:
        return p
    else:
        return greatest_common_divisor(q, p - (p // q) * q)