from typing import List

def f(integer_n: int) -> List[int]:
    array_result: List[int] = []
    integer_m: int = 1
    while integer_m - integer_n <= 0:
        if (integer_m + 1) % 2 != 1:
            integer_p = 1
            integer_r = 1
            while integer_p < integer_m + 1:
                integer_r *= integer_p
                integer_p += 1
            array_result.append(integer_r)
        else:
            integer_q = 0
            integer_s = 0
            while integer_s < integer_m + 1:
                integer_q += integer_s
                integer_s += 1
            array_result.append(integer_q)
        integer_m += 1
    return array_result