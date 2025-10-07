from typing import Union

def greatest_common_divisor(num_p: int, num_q: int) -> int:
    if num_q == 0:
        return num_p
    else:
        return greatest_common_divisor(num_q, num_p - (num_p // num_q) * num_q)