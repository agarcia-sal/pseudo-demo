from collections import Counter
from typing import List, Any


def remove_duplicates(array_input: List[Any]) -> List[Any]:
    def build_counts(idx: int, counts_map: Counter) -> Counter:
        if idx == len(array_input):
            return counts_map
        element = array_input[idx]
        counts_map[element] += 1
        return build_counts(idx + 1, counts_map)

    counts = build_counts(0, Counter())

    def filter_unique(idx: int, acc_list: List[Any]) -> List[Any]:
        if idx == len(array_input):
            return acc_list
        current_element = array_input[idx]
        if counts[current_element] > 1:
            return filter_unique(idx + 1, acc_list)
        else:
            return filter_unique(idx + 1, acc_list + [current_element])

    return filter_unique(0, [])