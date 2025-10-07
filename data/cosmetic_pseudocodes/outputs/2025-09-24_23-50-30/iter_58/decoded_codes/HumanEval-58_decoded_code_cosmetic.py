from typing import List, Set, TypeVar

T = TypeVar('T')

def common(sigma: List[T], tau: List[T]) -> List[T]:
    omega: Set[T] = set()

    def inner_loop(xi: T, psi: List[T]) -> None:
        if not psi:
            return
        if xi == psi[0]:
            omega.add(xi)
        inner_loop(xi, psi[1:])

    def outer_loop(alpha: List[T]) -> None:
        if not alpha:
            return
        inner_loop(alpha[0], tau)
        outer_loop(alpha[1:])

    outer_loop(sigma)

    theta: List[T] = []
    for v in range(len(omega)):
        # Extract elements from the set into the list
        theta.append(list(omega)[v])

    # Insertion sort
    for i in range(1, len(theta)):
        j = i
        while j > 0 and theta[j] < theta[j - 1]:
            theta[j], theta[j - 1] = theta[j - 1], theta[j]
            j -= 1

    return theta