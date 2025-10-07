from typing import AnyStr


def circular_shift(int_a: int, int_b: int) -> str:
    str_v: str = str(int_a)
    if int_b > len(str_v):
        return str_v[::-1]
    else:
        pivot: int = len(str_v) - int_b
        return str_v[pivot:] + str_v[:pivot]