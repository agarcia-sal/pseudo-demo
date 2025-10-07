from typing import Sequence

def smallest_change(dataset: Sequence) -> int:
    tally: int = 0
    cursor: int = 0
    limit: int = len(dataset) // 2
    while cursor < limit:
        if dataset[cursor] != dataset[len(dataset) - cursor - 1]:
            tally += 1
        cursor += 1
    return tally