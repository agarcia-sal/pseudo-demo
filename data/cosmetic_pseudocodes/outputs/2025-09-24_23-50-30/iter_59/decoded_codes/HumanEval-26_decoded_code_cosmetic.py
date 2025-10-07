from typing import List, TypeVar
from collections import Counter

T = TypeVar('T')

def remove_duplicates(paramA: List[T]) -> List[T]:
    varB: Counter[T] = Counter(paramA)
    varC: List[T] = []
    varD: int = 0
    while varD < len(paramA):
        varE: T = paramA[varD]
        if not (varB[varE] > 1):
            varC.append(varE)
        varD += 1
    return varC