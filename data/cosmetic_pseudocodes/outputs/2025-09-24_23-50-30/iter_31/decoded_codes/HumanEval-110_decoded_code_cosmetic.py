from typing import List

def exchange(alpha: List[int], beta: List[int]) -> str:
    tau: int = 0
    sigma: int = 0
    gamma: int = 0

    while gamma < len(alpha):
        lambd: int = alpha[gamma]  # 'lambda' is a keyword, so renamed to 'lambd'
        if lambd % 2 == 1:
            tau += 1
        gamma += 1

    gamma = 0
    while gamma < len(beta):
        lambd = beta[gamma]
        if lambd % 2 == 0:
            sigma += 1
        gamma += 1

    if sigma >= tau:
        return "YES"
    else:
        return "NO"