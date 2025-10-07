from typing import List

def separate_paren_groups(a: str) -> List[str]:
    b: List[str] = []
    c: List[str] = []
    d: int = 0

    i: int = 0
    while i < len(a):
        g = a[i]
        i += 1

        if g == '(':
            d += 1
            c.append(g)
        elif g == ')':
            d -= 1
            c.append(g)
            if d == 0:
                b.append(''.join(c))
                c.clear()
        # else: ignore any character that is not '(' or ')'

    return b