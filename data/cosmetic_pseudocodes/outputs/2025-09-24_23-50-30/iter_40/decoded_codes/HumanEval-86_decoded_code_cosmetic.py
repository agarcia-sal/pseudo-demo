from typing import List

def anti_shuffle(alpha: str) -> str:
    omega: List[str] = alpha.split(" ")
    delta: List[str] = []
    idx: int = 0
    while idx < len(omega):
        gamma: List[str] = sorted(list(omega[idx]))
        beta: str = "".join(gamma)
        delta.append(beta)
        idx += 1
    sigma: str = " ".join(delta)
    return sigma