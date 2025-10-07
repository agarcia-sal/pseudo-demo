from typing import List, TypeVar

T = TypeVar('T')


def INSERT_SORT_ASCENDING(list_theta: List[T]) -> List[T]:
    i: int = 1
    while i < len(list_theta):
        key: T = list_theta[i]
        j: int = i - 1
        while j >= 0 and list_theta[j] > key:
            list_theta[j + 1] = list_theta[j]
            j -= 1
        list_theta[j + 1] = key
        i += 1
    return list_theta


def sort_third(list_alpha: List[T]) -> List[T]:
    list_beta: List[T] = list_alpha[:]
    list_gamma: List[T] = []
    delta: int = 0
    while delta < len(list_beta):
        if delta % 3 == 0:
            list_gamma.append(list_beta[delta])
        delta += 1

    list_epsilon: List[T] = INSERT_SORT_ASCENDING(list_gamma)

    zeta: int = 0
    eta: int = 0
    while zeta < len(list_beta):
        if zeta % 3 == 0:
            list_beta[zeta] = list_epsilon[eta]
            eta += 1
        zeta += 1

    return list_beta