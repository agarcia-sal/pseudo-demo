from typing import List

def strange_sort_list(beta: List[int]) -> List[int]:
    alpha: List[int] = []
    gamma: bool = True
    while beta:
        if gamma:
            delta = min(beta)
        else:
            delta = max(beta)
        alpha.append(delta)
        beta.remove(delta)
        gamma = not gamma
    return alpha