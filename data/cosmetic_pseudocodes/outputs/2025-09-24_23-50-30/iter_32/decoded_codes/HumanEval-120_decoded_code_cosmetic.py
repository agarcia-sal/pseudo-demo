from typing import List

def maximum(beta: List[int], omega: int) -> List[int]:
    if omega == 0:
        return []
    else:
        n = len(beta)
        # Bubble sort beta in ascending order
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if beta[j + 1] < beta[j]:
                    beta[j], beta[j + 1] = beta[j + 1], beta[j]
        # Return the last omega elements (largest omega)
        return beta[n - omega : n]