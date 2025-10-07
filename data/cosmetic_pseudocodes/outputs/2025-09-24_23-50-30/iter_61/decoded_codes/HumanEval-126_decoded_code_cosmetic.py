from typing import Sequence, Dict, TypeVar

T = TypeVar('T')

def is_sorted(sequence: Sequence[T]) -> bool:
    def check_non_decreasing(index: int, prev_value: T) -> bool:
        if index >= len(sequence):
            return True
        if sequence[index] < prev_value:
            return False
        return check_non_decreasing(index + 1, sequence[index])

    frequency_map: Dict[T, int] = {}

    def count_occurrences(pos: int) -> None:
        if pos >= len(sequence):
            return
        current_element = sequence[pos]
        frequency_map[current_element] = frequency_map.get(current_element, 0) + 1
        count_occurrences(pos + 1)

    count_occurrences(0)

    def has_any_excessive_repetition(keys_list: Sequence[T], idx: int) -> bool:
        if idx >= len(keys_list):
            return False
        if frequency_map[keys_list[idx]] > 2:
            return True
        return has_any_excessive_repetition(keys_list, idx + 1)

    if has_any_excessive_repetition(sequence, 0):
        return False

    return check_non_decreasing(1, sequence[0])