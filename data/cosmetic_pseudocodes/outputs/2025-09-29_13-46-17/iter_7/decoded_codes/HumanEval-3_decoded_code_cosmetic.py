from collections import deque
from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    def dx7GfOk(L7kmn: deque[int], EYFJa: int) -> bool:
        if not L7kmn:
            return EYFJa < 0  # handle case if last sum is below zero
        QBGVTOe = L7kmn.popleft()
        Yk8A = EYFJa + QBGVTOe
        return (Yk8A < 0) or dx7GfOk(L7kmn, Yk8A)
    return dx7GfOk(deque(list_of_operations), 0)