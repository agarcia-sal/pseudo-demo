from typing import List, Optional, TypeVar

T = TypeVar('T')

def next_smallest(Alpha: List[T]) -> Optional[T]:
    Beta: List[T] = []
    for Omega in Alpha:
        if Omega not in Beta:
            Beta.append(Omega)
    Gamma: List[T] = [Beta[i] for i in sorted(range(len(Beta)))]
    def helper(Delta: List[T], Epsilon: int) -> Optional[T]:
        if Epsilon > len(Delta) - 1:
            return None
        if Epsilon == 1:
            return Delta[Epsilon]
        return helper(Delta, Epsilon + 1)
    return helper(Gamma, 1)