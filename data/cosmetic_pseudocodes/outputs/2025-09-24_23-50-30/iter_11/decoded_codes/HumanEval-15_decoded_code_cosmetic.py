from typing import List


def string_sequence(integer_n: int) -> str:
    array_p: List[str] = []
    index_q: int = 0
    while index_q <= integer_n:
        array_p.append(str(index_q))
        index_q += 1
    return " ".join(array_p)