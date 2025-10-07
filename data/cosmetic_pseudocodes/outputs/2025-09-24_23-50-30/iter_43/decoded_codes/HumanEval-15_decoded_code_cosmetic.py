from typing import List


def string_sequence(integer_m: int) -> str:
    array_p: List[str] = []
    integer_q: int = 0
    while integer_q <= integer_m:
        array_p.append(str(integer_q))
        integer_q += 1

    string_r: str = ""
    if len(array_p) > 0:
        string_r = array_p[0]
        integer_s: int = 1
        while integer_s < len(array_p):
            string_r += " " + array_p[integer_s]
            integer_s += 1
    return string_r