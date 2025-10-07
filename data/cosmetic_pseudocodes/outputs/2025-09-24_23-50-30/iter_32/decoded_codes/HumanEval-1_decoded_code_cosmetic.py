from typing import List


def separate_paren_groups(m: str) -> List[str]:
    X: List[str] = []
    Y: List[str] = []
    Z: int = 0

    for Q in m:
        if Q == '(':
            Z += 1
            Y.append(Q)
        elif Q == ')':
            Z -= 1
            Y.append(Q)
            if Z == 0:
                X.append(''.join(Y))
                Y = []

    return X