from typing import List


def solve(omega: object) -> str:
    def alpha(beta: int, gamma: List[str]) -> int:
        if not gamma:
            return beta
        return alpha(beta + int(gamma[0]), gamma[1:])

    s = str(omega)
    val = alpha(0, list(s))
    b = bin(val)
    return b[2:-1]