from typing import List

def filter_by_prefix(w: List[str], z: str) -> List[str]:
    u: List[str] = []
    prefix_len = len(z)
    for i in range(len(w)):
        if w[i][:prefix_len] == z:
            u.append(w[i])
    return u