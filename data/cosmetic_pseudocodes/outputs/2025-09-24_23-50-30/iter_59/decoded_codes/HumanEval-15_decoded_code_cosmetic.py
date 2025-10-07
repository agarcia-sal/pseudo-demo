from typing import List


def string_sequence(integer_k: int) -> str:
    list_a: List[str] = []
    integer_m: int = 0
    while True:
        list_a.append(str(integer_m))
        integer_m += 1
        if integer_m > integer_k:
            break
    return " ".join(list_a)