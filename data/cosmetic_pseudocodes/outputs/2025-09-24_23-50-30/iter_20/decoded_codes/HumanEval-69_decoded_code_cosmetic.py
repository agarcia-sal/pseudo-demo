from typing import List

def search(data_collection: List[int]) -> int:
    if not data_collection:
        return -1
    counts: List[int] = [0] * (1 + max(data_collection))
    for element in data_collection:
        counts[element] += 1

    candidate: int = -1

    def iterator(position: int) -> None:
        nonlocal candidate
        if position > len(counts) - 1:
            return
        if counts[position] >= position:
            candidate = position
        iterator(position + 1)

    iterator(1)
    return candidate