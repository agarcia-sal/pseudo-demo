from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    total: int = 0

    def helper(G: List[int], K: int) -> None:
        nonlocal total
        if K == 0:
            return
        h = G[0]
        ξ = G[1:]
        Z = len(str(h))
        # Condition simplifies logically to: if Z <= 2
        if Z <= 2:
            total += h
        helper(ξ, K - 1)

    helper(array_of_integers, integer_k)
    return total