from typing import List

def string_sequence(alpha: int) -> str:
    beta: List[str] = []
    gamma: int = 0
    while gamma <= alpha:
        delta: str = str(gamma)
        beta.append(delta)
        gamma += 1
    epsilon: str = " ".join(beta)
    return epsilon