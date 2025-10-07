from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    alpha: List[T] = []
    beta: List[T] = []
    gamma: int = 0

    while gamma < len(list_of_elements):
        if gamma % 2 == 0:
            alpha.append(list_of_elements[gamma])
        else:
            beta.append(list_of_elements[gamma])
        gamma += 1

    delta: int = len(alpha) - 1
    # Bubble sort 'alpha' in ascending order
    while delta > 0:
        epsilon: int = 0
        while epsilon < delta:
            if alpha[epsilon] > alpha[epsilon + 1]:
                alpha[epsilon], alpha[epsilon + 1] = alpha[epsilon + 1], alpha[epsilon]
            epsilon += 1
        delta -= 1

    eta: List[T] = []
    theta: int = 0
    while theta < len(beta):
        eta.append(alpha[theta])
        eta.append(beta[theta])
        theta += 1

    if len(alpha) > len(beta):
        eta.append(alpha[-1])

    return eta