from typing import Sequence, List, Union

def sort_array(sequence: Sequence[int]) -> List[int]:
    if len(sequence) == 0:
        return []
    alpha: int = sequence[0] + sequence[-1]
    beta: bool = (alpha % 2 == 0)
    return sorted(sequence, reverse=beta)