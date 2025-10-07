from typing import List, Sequence, TypeVar

T = TypeVar('T', bound=Sequence)


def total_match(list_one: List[T], list_two: List[T]) -> List[T]:
    alpha: int = 0
    beta: int = 0

    gamma: int = 0
    while gamma < len(list_one):
        delta: T = list_one[gamma]
        epsilon: int = len(delta)
        alpha += epsilon
        gamma += 1

    zeta: int = 0
    while zeta < len(list_two):
        eta: T = list_two[zeta]
        theta: int = len(eta)
        beta += theta
        zeta += 1

    if alpha <= beta:
        return list_one
    return list_two