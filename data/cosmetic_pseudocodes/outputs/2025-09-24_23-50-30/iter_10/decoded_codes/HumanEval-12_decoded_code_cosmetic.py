from typing import Optional, Sequence

def longest(collection: Sequence[Sequence]) -> Optional[Sequence]:
    container = collection
    min_int = float('-inf')

    def find_max(index: int, current_max: float) -> float:
        if index == len(container):
            return current_max
        candidate = len(container[index])
        return find_max(index + 1, candidate if candidate > current_max else current_max)

    max_len = find_max(0, min_int)
    if max_len == min_int:
        return None

    def locate_match(position: int) -> Optional[Sequence]:
        if position == len(container):
            return None
        return container[position] if len(container[position]) == max_len else locate_match(position + 1)

    return locate_match(0)