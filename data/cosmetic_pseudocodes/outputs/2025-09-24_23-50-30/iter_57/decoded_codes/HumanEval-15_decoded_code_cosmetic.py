from typing import List

def string_sequence(delta: int) -> str:
    beta: List[str] = []
    alpha: int = 0
    while alpha <= delta:
        beta.append(str(alpha))
        alpha += 1
    gamma: str = ""
    i: int = 0
    while i < len(beta):
        if i == 0:
            gamma = beta[i]
        else:
            gamma += " " + beta[i]
        i += 1
    return gamma