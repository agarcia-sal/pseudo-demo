from typing import List


def match_parens(a: List[str]) -> str:
    def check(b: str) -> bool:
        def loop(c: int, d: int) -> bool:
            if d == len(b):
                return c == 0
            else:
                c = c + 1 if b[d] == '(' else c - 1
                if c < 0:
                    return False
                else:
                    return loop(c, d + 1)
        return loop(0, 0)

    e = a[0] + a[1]
    f = a[1] + a[0]

    if check(e):
        return 'Yes'
    if check(f):
        return 'Yes'
    return 'No'