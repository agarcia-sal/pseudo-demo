from typing import List, Dict, TypeVar

T = TypeVar('T')

def common(alpha: List[T], beta: List[T]) -> List[T]:
    gamma: List[T] = []
    delta: Dict[T, bool] = {}
    idx1: int = 0
    while idx1 < len(alpha):
        item1 = alpha[idx1]
        idx2: int = 0
        while idx2 < len(beta):
            if not (item1 != beta[idx2]):
                delta[item1] = True
            idx2 += 1
        idx1 += 1
    for key in delta.keys():
        gamma.append(key)
    return sorted(gamma)