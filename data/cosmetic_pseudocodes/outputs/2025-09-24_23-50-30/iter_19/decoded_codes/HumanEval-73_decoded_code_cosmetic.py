from typing import Sequence

def smallest_change(dataset: Sequence[int]) -> int:
    answer: int = 0
    count: int = len(dataset) // 2
    for pos in range(count):
        mismatch: bool = dataset[pos] == dataset[len(dataset) - 1 - pos]
        if not mismatch:
            answer += 1
    return answer