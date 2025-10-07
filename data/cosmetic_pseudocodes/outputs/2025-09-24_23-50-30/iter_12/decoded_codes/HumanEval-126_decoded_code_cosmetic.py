from collections import defaultdict
from typing import List, Union


def is_sorted(source_array: List[Union[int, float]]) -> bool:
    frequency_map: defaultdict[Union[int, float], int] = defaultdict(int)
    for element in source_array:
        frequency_map[element] += 1
    if any(count > 2 for count in frequency_map.values()):
        return False

    def predicate(index: int) -> bool:
        return not (source_array[index] < source_array[index - 1])

    for idx in range(1, len(source_array)):
        if not predicate(idx):
            return False
    return True