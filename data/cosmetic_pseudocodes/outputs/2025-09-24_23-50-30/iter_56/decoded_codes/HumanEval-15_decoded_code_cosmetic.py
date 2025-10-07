from typing import List


def string_sequence(integer_f: int) -> str:
    array_g: List[str] = []
    integer_h: int = 0
    while integer_h <= integer_f:
        array_g.append(str(integer_h))
        integer_h += 1
    string_i: str = ""
    integer_j: int = 0
    while integer_j < len(array_g):
        if integer_j == 0:
            string_i = array_g[integer_j]
        else:
            string_i += " " + array_g[integer_j]
        integer_j += 1
    return string_i