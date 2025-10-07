from typing import List

def filter_by_prefix(beta: List[str], gamma: str) -> List[str]:
    delta: List[str] = []
    for epsilon in beta:
        if epsilon[:len(gamma)] == gamma:
            delta.append(epsilon)
    return delta