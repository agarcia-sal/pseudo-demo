from typing import List

def get_positive(variables: List[float]) -> List[float]:
    store: List[float] = []
    idx: int = 0
    while idx < len(variables):
        if variables[idx] > 0:
            store.append(variables[idx])
        idx += 1
    return store