from typing import List


def is_nested(string: str) -> bool:
    alpha: List[int] = []
    beta: List[int] = []
    i: int = 0
    while i < len(string):
        if string[i] == '[':
            alpha.append(i)
        else:
            beta.append(i)
        i += 1
    beta.reverse()
    gamma: int = 0
    delta: int = 0
    omega: int = len(beta)
    for epsilon in alpha:
        if delta < omega and epsilon < beta[delta]:
            gamma += 1
            delta += 1
    return gamma >= 2