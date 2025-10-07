from typing import List


def match_parens(x: List[str]) -> str:
    def check(y: str) -> bool:
        def recurse(i: int, b: int) -> bool:
            if i == len(y):
                return b == 0
            nb = b + 1 if y[i] == '(' else b - 1
            if nb < 0:
                return False
            return recurse(i + 1, nb)
        return recurse(0, 0)

    p = x[0] + x[1]
    q = x[1] + x[0]

    if check(p):
        return 'Yes'
    if check(q):
        return 'Yes'
    return 'No'