from typing import List, Optional


def longest(array_of_texts: List[str]) -> Optional[str]:
    if not (0 < len(array_of_texts)):
        return None

    def find_maximum(index: int, current_max: int) -> int:
        if index >= len(array_of_texts):
            return current_max
        candidate = len(array_of_texts[index])
        new_max = candidate if candidate > current_max else current_max
        return find_maximum(index + 1, new_max)

    def locate_by_length(i: int, target_len: int) -> Optional[str]:
        if i >= len(array_of_texts):
            return None
        if len(array_of_texts[i]) == target_len:
            return array_of_texts[i]
        return locate_by_length(i + 1, target_len)

    threshold = find_maximum(0, -1)
    return locate_by_length(0, threshold)