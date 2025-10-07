from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    alpha: List[T] = []
    beta: int = 0
    while beta < len(list_of_elements):
        if beta % 2 == 0:
            alpha.append(list_of_elements[beta])
        beta += 1

    gamma: List[T] = []
    delta: int = 1
    while delta < len(list_of_elements):
        if delta % 2 == 1:
            gamma.append(list_of_elements[delta])
        delta += 1

    sorted_alpha = sorted(alpha)

    zeta: List[T] = []
    eta: int = 0
    while eta < len(gamma) and eta < len(sorted_alpha):
        zeta.append(sorted_alpha[eta])
        zeta.append(gamma[eta])
        eta += 1

    if len(sorted_alpha) > len(gamma):
        zeta.append(sorted_alpha[-1])

    return zeta