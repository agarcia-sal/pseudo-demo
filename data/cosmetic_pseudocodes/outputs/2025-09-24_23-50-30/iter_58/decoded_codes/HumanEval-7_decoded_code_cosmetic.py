from typing import List

def filter_by_substring(beta: List[str], gamma: str) -> List[str]:
    delta: List[str] = []
    for epsilon in beta:
        if gamma in epsilon:
            delta.append(epsilon)
    return delta