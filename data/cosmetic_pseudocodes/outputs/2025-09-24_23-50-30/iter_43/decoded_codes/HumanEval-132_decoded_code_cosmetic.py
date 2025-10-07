from typing import List


def is_nested(alpha: str) -> bool:
    v: int = 0
    w: int = 0  # unused, but preserved as per pseudocode
    Y: List[int] = []
    X: List[int] = []
    Z: int = len(alpha) - 1
    while v <= Z:
        if alpha[v] == '[':
            Y.append(v)
        else:
            X.append(v)
        v += 1

    l: int = len(X)
    R: int = l - 1
    S: int = 0
    T: int  # temporary variable to swap
    while R >= 0:
        T = X[R]
        X[R] = X[S]
        X[S] = T
        R -= 1
        S += 1

    U: int = len(Y)
    Q: int = 0
    P: int = 0
    O: int = 0
    while Q < U:
        if P < len(X) and Y[Q] < X[P]:
            O += 1
            P += 1
        Q += 1

    return not (O < 2)