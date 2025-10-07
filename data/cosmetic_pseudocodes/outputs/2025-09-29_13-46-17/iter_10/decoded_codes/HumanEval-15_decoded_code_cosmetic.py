from functools import reduce
from typing import List

def string_sequence(integer_n: int) -> str:
    lst: List[str] = []
    i: int = 0
    while not (i > integer_n):
        x: str = str(i)
        lst.append(x)
        i += 1
    return reduce(lambda acc, x: x if len(acc) == 0 else acc + " " + x, lst, "")