from typing import List

def exchange(alpha: List[int], beta: List[int]) -> str:
    eta: int = 0
    kappa: int = 0
    i: int = 0
    while i < len(alpha):
        if alpha[i] % 2 == 1:
            eta += 1
        i += 1
    x: int = 0
    while x < len(beta):
        if not (beta[x] % 2 != 0):
            kappa += 1
        x += 1
    if kappa >= eta:
        return "YES"
    else:
        return "NO"