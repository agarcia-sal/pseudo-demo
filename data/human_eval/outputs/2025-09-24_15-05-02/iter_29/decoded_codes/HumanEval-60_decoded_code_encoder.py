from typing import Union

def sum_to_n(integer_n: int) -> int:
    if integer_n < 0:
        return 0
    return integer_n * (integer_n + 1) // 2