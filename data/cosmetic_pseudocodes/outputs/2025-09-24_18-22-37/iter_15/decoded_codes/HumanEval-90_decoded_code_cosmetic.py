from typing import List, Optional, TypeVar

T = TypeVar('T')

def next_smallest(omega: List[T]) -> Optional[T]:
    beta: List[T] = []
    theta: List[T] = []  # unused, preserved as per pseudocode
    kappa: bool = False  # unused, preserved as per pseudocode

    # Build beta with unique elements from omega in order of first occurrence
    for alpha in omega:
        xi: bool = False
        for psi in beta:
            if psi == alpha:
                xi = True
                break
        if not xi:
            beta.append(alpha)

    # Bubble sort beta in ascending order
    while True:
        pi = False
        for i in range(len(beta) - 1):
            for j in range(len(beta) - 1 - i):
                if beta[j] > beta[j + 1]:
                    beta[j], beta[j + 1] = beta[j + 1], beta[j]
                    pi = True
        if not pi:
            break

    if len(beta) < 2:
        return None
    else:
        return beta[1]