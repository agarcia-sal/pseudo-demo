from typing import List, Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def total_match(list_one: List[T], list_two: List[T]) -> List[T]:
    alpha: int = 0
    beta: int = 0

    pointer_a: int = 0
    while pointer_a < len(list_one):
        gamma: T = list_one[pointer_a]
        delta: int = len(gamma)
        alpha += delta
        pointer_a += 1

    pointer_b: int = 0
    while pointer_b < len(list_two):
        epsilon: T = list_two[pointer_b]
        zeta: int = len(epsilon)
        beta += zeta
        pointer_b += 1

    if not (beta < alpha):
        return list_one
    return list_two