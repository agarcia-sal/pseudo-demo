from typing import List, TypeVar

T = TypeVar("T")

def sort_even(X: List[T]) -> List[T]:
    A = [e for i, e in enumerate(X) if i % 2 == 0]
    B = [f for j, f in enumerate(X) if j % 2 == 1]
    A.sort()
    Y: List[T] = []
    index = 0
    limit = min(len(A), len(B))
    while index < limit:
        Y.append(A[index])
        Y.append(B[index])
        index += 1
    if len(A) > len(B):
        Y.append(A[-1])
    return Y