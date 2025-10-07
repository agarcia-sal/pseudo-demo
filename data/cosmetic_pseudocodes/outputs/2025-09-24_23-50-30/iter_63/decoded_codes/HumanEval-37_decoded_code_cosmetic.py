from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    A: List[T] = []
    B: List[T] = []
    C: int = 0
    while C < len(list_of_elements):
        if C % 2 == 0:
            A.append(list_of_elements[C])
        else:
            B.append(list_of_elements[C])
        C += 1
    A.sort()
    D: List[T] = []
    E: int = 0
    limit = min(len(A), len(B))
    while E < limit:
        D.append(A[E])
        D.append(B[E])
        E += 1
    if len(A) > len(B):
        D.append(A[-1])
    return D