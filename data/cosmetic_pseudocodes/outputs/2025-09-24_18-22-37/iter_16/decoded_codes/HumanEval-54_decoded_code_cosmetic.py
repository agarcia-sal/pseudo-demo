from typing import Sequence


def same_chars(alpha: Sequence[str], beta: Sequence[str]) -> bool:
    setA: set[str] = set()
    setB: set[str] = set()

    i: int = 0
    while i < len(alpha):
        c = alpha[i]
        setA.add(c)
        i += 1

    i = 0
    while i < len(beta):
        c = beta[i]
        setB.add(c)
        i += 1

    if setA != setB:
        return False

    return True