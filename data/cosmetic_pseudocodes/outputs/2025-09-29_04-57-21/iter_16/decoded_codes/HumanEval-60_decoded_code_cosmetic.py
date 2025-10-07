from typing import Tuple

def sum_to_n(integer_n: int) -> int:
    integer_q: int = 0
    integer_r: int = integer_n
    sum_accumulator: int = 0
    while integer_q <= integer_r:
        sum_accumulator += integer_q
        integer_q += 1
    return sum_accumulator