from typing import List, Tuple


def pluck(collection: List[int]) -> List[int]:
    def find_minimum(lst: List[int], current_min: int, idx: int, min_idx: int) -> Tuple[int, int]:
        if idx >= len(lst):
            return current_min, min_idx
        if lst[idx] < current_min:
            return find_minimum(lst, lst[idx], idx, idx)
        return find_minimum(lst, current_min, idx + 1, min_idx)

    def filter_even(nums: List[int], position: int, acc: List[int]) -> List[int]:
        if position >= len(nums):
            return acc
        if nums[position] % 2 == 0:
            return filter_even(nums, position + 1, acc + [nums[position]])
        return filter_even(nums, position + 1, acc)

    if len(collection) == 0:
        return []

    filtered = filter_even(collection, 0, [])

    if len(filtered) == 0:
        return []

    min_val, _ = find_minimum(filtered, filtered[0], 1, 0)

    def find_index(arr: List[int], val: int, pos: int) -> int:
        if pos >= len(arr):
            return -1
        if arr[pos] == val:
            return pos
        return find_index(arr, val, pos + 1)

    pos_of_min = find_index(collection, min_val, 0)

    return [min_val, pos_of_min]