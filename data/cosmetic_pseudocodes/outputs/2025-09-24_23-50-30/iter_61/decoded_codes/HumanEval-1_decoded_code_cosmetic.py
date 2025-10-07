from typing import List

def separate_paren_groups(q: str) -> List[str]:
    nn: List[str] = []
    xx: List[str] = []
    rr: int = 0

    while True:
        if len(q) == 0:
            break
        oo: str = q[0]
        q = q[1:]
        if oo == '(':
            rr += 1
            xx.append(oo)
        elif oo == ')':
            rr -= 1
            xx.append(oo)
            if rr == 0:
                nn.append(''.join(xx))
                xx = []

    return nn