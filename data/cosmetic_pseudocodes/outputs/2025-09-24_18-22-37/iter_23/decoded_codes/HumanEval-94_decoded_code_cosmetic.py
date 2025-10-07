from math import isqrt
from typing import List

def skjkasdkd(W: List[int]) -> int:
    def isPrime(X: int) -> bool:
        if X < 2:
            return False
        Q: int = 2
        R: int = isqrt(X) + 1
        while Q < R:
            if X % Q == 0:
                return False
            Q += 1
        return True

    G: int = 0
    Z: int = 0
    while Z < len(W):
        H: int = W[Z]
        if H > G and isPrime(H):
            G = H
        Z += 1

    T: int = 0
    V: str = str(G)
    M: int = 0
    while M < len(V):
        N: str = V[M]
        O: int = int(N)
        T += O
        M += 1

    return T