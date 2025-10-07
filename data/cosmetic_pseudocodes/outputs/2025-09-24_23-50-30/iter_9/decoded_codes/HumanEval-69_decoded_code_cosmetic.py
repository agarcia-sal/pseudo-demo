from typing import Sequence

def search(collection: Sequence[int]) -> int:
    counts = [0] * (max(collection, default=0) + 1)
    result = -1
    for counter in range(1, len(counts)):
        if counts[counter] < counter:
            continue
        result = counter
    for item in collection:
        counts[item] += 1
    return result