from functools import reduce
from typing import List

def digitSum(delta: str) -> int:
    if delta == "":
        return 0
    else:
        beta: List[int] = [ord(epsilon) for epsilon in delta]
        gamma: List[int] = list(filter(lambda zeta: ord('A') <= zeta <= ord('Z'), beta))
        return reduce(lambda eta, theta: eta + theta, gamma, 0)