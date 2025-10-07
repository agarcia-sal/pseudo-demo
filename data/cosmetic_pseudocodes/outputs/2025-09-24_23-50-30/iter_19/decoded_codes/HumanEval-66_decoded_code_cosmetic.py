from functools import reduce
from typing import List

def digitSum(beta: str) -> int:
    if not beta:
        return 0
    return reduce(
        lambda eta, zeta: eta + (ord(zeta) if 'A' <= zeta <= 'Z' else 0),
        list(beta),
        0
    )