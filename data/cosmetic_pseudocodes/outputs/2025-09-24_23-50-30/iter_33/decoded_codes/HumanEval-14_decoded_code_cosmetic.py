from typing import List

def all_prefixes(beta: str) -> List[str]:
    omega: List[str] = []
    theta: int = 0
    while theta < len(beta):
        gamma: str = beta[:theta + 1]
        omega.append(gamma)
        theta += 1
    return omega