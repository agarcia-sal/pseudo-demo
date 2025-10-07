from typing import List

def sort_array(container: List[int]) -> List[int]:
    if len(container) == 0:
        return []
    alpha: int = container[0]
    beta: int = container[-1]
    gamma: int = alpha + beta
    delta: bool = (gamma % 2 == 0)
    return sorted(container, reverse=delta)