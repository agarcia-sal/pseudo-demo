from typing import Sequence, Dict, TypeVar

T = TypeVar('T')

def is_sorted(sequence: Sequence[T]) -> bool:
    def count_occurrences(arr: Sequence[T], idx: int, acc: Dict[T, int]) -> Dict[T, int]:
        if idx >= len(arr):
            return acc
        key = arr[idx]
        acc[key] = acc.get(key, 0) + 1
        return count_occurrences(arr, idx + 1, acc)

    def any_value_exceeds_two(freq_map: Dict[T, int], keys: Sequence[T], i: int) -> bool:
        if i >= len(keys):
            return False
        return (freq_map.get(keys[i], 0) > 2) or any_value_exceeds_two(freq_map, keys, i + 1)

    def is_non_decreasing(arr: Sequence[T], pos: int) -> bool:
        if pos >= len(arr):
            return True
        return (arr[pos - 1] <= arr[pos]) and is_non_decreasing(arr, pos + 1)

    frequency_map = count_occurrences(sequence, 0, {})
    keys_list = sequence

    if any_value_exceeds_two(frequency_map, keys_list, 0):
        return False
    if is_non_decreasing(sequence, 1):
        return True
    return False