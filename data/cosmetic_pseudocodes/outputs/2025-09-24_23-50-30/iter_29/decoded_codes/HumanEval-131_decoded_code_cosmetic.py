from functools import reduce
from typing import List

def digits(n: int) -> int:
    arr: List[int] = [int(x) for x in str(n) if int(x) % 2 == 1]
    res: int = 0 if len(arr) == 0 else reduce(lambda a, b: a * b, arr, 1)
    return res