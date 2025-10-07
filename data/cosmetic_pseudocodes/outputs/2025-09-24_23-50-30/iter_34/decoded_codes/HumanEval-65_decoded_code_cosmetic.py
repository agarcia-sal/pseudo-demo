from typing import List


def circular_shift(integer_a: int, integer_b: int) -> str:
    list_q: List[str] = list(str(integer_a))
    if not (integer_b <= len(list_q)):
        return "".join(reversed(list_q))
    else:
        integer_c: int = len(list_q) - integer_b
        list_m: List[str] = list_q[integer_c:]
        list_n: List[str] = list_q[:integer_c]
        return "".join(list_m + list_n)