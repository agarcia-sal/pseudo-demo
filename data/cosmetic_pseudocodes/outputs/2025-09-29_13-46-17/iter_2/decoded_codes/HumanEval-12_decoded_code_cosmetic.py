from typing import List, Optional


def longest(list_of_strings: List[str]) -> Optional[str]:
    def find_max_len(items: List[str], idx: int, current_max: int) -> int:
        if idx >= len(items):
            return current_max
        candidate = len(items[idx])
        return find_max_len(items, idx + 1, candidate if candidate > current_max else current_max)

    def find_longest_match(items: List[str], length_target: int, index: int) -> Optional[str]:
        if index >= len(items):
            return None
        elif len(items[index]) == length_target:
            return items[index]
        else:
            return find_longest_match(items, length_target, index + 1)

    if len(list_of_strings) == 0:
        return None

    max_len = find_max_len(list_of_strings, 0, -1)
    return find_longest_match(list_of_strings, max_len, 0)