from typing import List

def sort_array(sequence: List[int]) -> List[int]:
    if len(sequence) == 0:
        return []
    alpha: int = sequence[0] + sequence[-1]
    beta: bool = (alpha % 2 == 0)
    gamma: List[int] = sequence
    return sorted(gamma, reverse=beta)