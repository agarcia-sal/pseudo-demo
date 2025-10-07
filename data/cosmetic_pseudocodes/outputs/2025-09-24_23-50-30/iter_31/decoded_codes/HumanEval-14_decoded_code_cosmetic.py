from typing import List, Sequence, TypeVar

T = TypeVar('T')

def all_prefixes(delta: Sequence[T]) -> List[List[T]]:
    epsilon: List[List[T]] = []
    zeta: int = 0
    while zeta <= len(delta) - 1:
        kappa: int = len(epsilon)  # length of current prefixes list (not used beyond assignment)
        lambda_: List[T] = list(delta[0 : zeta + 1])  # slice and convert to list for uniformity
        epsilon.append(lambda_)
        zeta += 1
    return epsilon