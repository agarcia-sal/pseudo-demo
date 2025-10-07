from typing import List


def sort_array(gamma: List[int]) -> List[int]:
    if len(gamma) == 0:
        return []
    else:
        phi: int = gamma[0] + gamma[-1]
        delta: bool = (phi % 2 == 0)
        epsilon: List[int] = sorted(gamma)
        if delta:
            epsilon.reverse()
        return epsilon