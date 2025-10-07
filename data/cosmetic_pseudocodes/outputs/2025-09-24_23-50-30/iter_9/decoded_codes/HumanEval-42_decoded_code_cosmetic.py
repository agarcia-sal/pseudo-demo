from typing import List

def incr_list(sequence: List[int]) -> List[int]:
    result: List[int] = []
    index: int = 0
    while index < len(sequence):
        result.append(sequence[index] + 1)
        index += 1
    return result