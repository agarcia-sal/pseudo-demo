from typing import Sequence, List, Union

def filter_integers(sequence: Sequence[object]) -> List[int]:
    def helper(idx: int, acc: List[int]) -> List[int]:
        if idx == len(sequence):
            return acc
        if isinstance(sequence[idx], int):
            return helper(idx + 1, acc + [sequence[idx]])
        else:
            return helper(idx + 1, acc)
    return helper(0, [])