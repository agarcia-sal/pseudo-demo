from typing import Iterable, Optional


def search(iterator: Iterable[int]) -> int:
    # Convert iterable to a list to allow multiple passes and indexing
    elements = list(iterator)
    if not elements:
        return -1

    max_elem = max(elements)
    counts = [0] * (max_elem + 1)

    for elem in elements:
        counts[elem] += 1

    result = -1
    pos = len(counts) - 1
    while pos >= 1:
        if counts[pos] >= pos:
            result = pos
        pos -= 1

    return result