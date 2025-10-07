from typing import List, Optional

def search(alpha: List[int]) -> int:
    delta: List[int] = [0] * (max(alpha) + 1 if alpha else 1)

    def accumulate_beta(epsilon: List[int]) -> None:
        if not epsilon:
            return
        delta[epsilon[0]] += 1
        accumulate_beta(epsilon[1:])

    accumulate_beta(alpha)
    gamma: int = -1

    def find_delta(lmbda: int) -> None:
        nonlocal gamma
        if lmbda > len(delta) - 1:
            return
        if delta[lmbda] >= lmbda:
            gamma = lmbda
        find_delta(lmbda + 1)

    find_delta(1)
    return gamma