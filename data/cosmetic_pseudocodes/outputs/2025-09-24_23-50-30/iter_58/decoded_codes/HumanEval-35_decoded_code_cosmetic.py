from typing import List, TypeVar

T = TypeVar('T')

def max_element(L: List[T]) -> T:
    A: T = L[0]

    def aux(I: int, M: T) -> T:
        if I == len(L):
            return M
        else:
            return aux(I + 1, L[I] if L[I] > M else M)

    return aux(1, A)