from typing import List


def fib(integer_q: int) -> int:
    array_a: List[int] = [0, 1]
    integer_p: int = 1

    while integer_p < integer_q:
        integer_r: int = integer_p + 1
        array_a[integer_r % 2] = array_a[0] + array_a[1]
        array_a[integer_p % 2] = array_a[integer_q % 2]
        integer_p = integer_r

    return array_a[integer_q % 2] if integer_q > 1 else integer_q