from typing import List

def fibfib(integer_q: int) -> int:
    array_p: List[int] = [0, 0, 1]
    integer_r: int = 3
    while integer_r <= integer_q:
        array_p.append(array_p[integer_r - 1] + array_p[integer_r - 2] + array_p[integer_r - 3])
        integer_r += 1
    return array_p[integer_q]