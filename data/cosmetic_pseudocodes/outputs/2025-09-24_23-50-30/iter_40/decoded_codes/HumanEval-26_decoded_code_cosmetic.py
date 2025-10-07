from collections import Counter
from typing import List, Any


def remove_duplicates(array_input: List[Any]) -> List[Any]:
    frequency_map: Counter[Any] = Counter(array_input)

    def build_result(current_index: int, acc: List[Any]) -> List[Any]:
        if current_index >= len(array_input):
            return acc
        item = array_input[current_index]
        if frequency_map[item] <= 1:
            return build_result(current_index + 1, acc + [item])
        return build_result(current_index + 1, acc)

    return build_result(0, [])