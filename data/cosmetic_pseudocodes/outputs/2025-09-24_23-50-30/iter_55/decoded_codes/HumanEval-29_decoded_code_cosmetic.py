from typing import List

def filter_by_prefix(array_alpha: List[str], beta: str) -> List[str]:
    filtered_beta: List[str] = []
    idx: int = 0
    while idx < len(array_alpha):
        if array_alpha[idx].startswith(beta):
            filtered_beta.append(array_alpha[idx])
        idx += 1
    return filtered_beta