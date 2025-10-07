from typing import List

def exchange(alpha: List[int], beta: List[int]) -> str:
    sigma: int = 0
    tau: int = 0

    def recursive_sigma(idx: int) -> None:
        nonlocal sigma
        if idx >= len(alpha):
            return
        if (alpha[idx] & 1) == 1:
            sigma += 1
        recursive_sigma(idx + 1)

    def recursive_tau(idx: int) -> None:
        nonlocal tau
        if idx >= len(beta):
            return
        if (beta[idx] & 1) == 0:
            tau += 1
        recursive_tau(idx + 1)

    recursive_sigma(0)
    recursive_tau(0)

    if tau >= sigma:
        return "YES"
    return "NO"