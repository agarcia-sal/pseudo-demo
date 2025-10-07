from typing import List

def derivative(alpha: List[float]) -> List[float]:
    beta: List[float] = []
    for gamma in range(1, len(alpha)):
        beta.append(alpha[gamma] * gamma)
    return beta