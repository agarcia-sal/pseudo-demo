from typing import List


def sort_array(container: List[int]) -> List[int]:
    length = len(container)
    if length == 0:
        return []
    temp = (container[0] + container[-1]) % 2 == 0
    return sorted(container, reverse=temp)