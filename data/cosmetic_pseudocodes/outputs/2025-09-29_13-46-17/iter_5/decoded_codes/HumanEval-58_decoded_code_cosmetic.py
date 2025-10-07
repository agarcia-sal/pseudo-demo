from typing import List, Set, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    accumulator: Set[T] = set()
    i: int = 0

    def inner_loop(value: T, idx: int, collected: Set[T]) -> Set[T]:
        if idx >= len(list2):
            return collected
        if value != list2[idx]:
            return inner_loop(value, idx + 1, collected)
        updated = collected | {value}
        return inner_loop(value, idx + 1, updated)

    while i < len(list1):
        accumulator = inner_loop(list1[i], 0, accumulator)
        i += 1

    result_array: List[T] = []
    for key in accumulator:
        result_array.append(key)

    def merge_sort(arr: List[T]) -> List[T]:
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)

        merged: List[T] = []
        l_idx = 0
        r_idx = 0
        while l_idx < len(sorted_left) and r_idx < len(sorted_right):
            if sorted_left[l_idx] < sorted_right[r_idx]:
                merged.append(sorted_left[l_idx])
                l_idx += 1
            else:
                merged.append(sorted_right[r_idx])
                r_idx += 1

        while l_idx < len(sorted_left):
            merged.append(sorted_left[l_idx])
            l_idx += 1

        while r_idx < len(sorted_right):
            merged.append(sorted_right[r_idx])
            r_idx += 1

        return merged

    return merge_sort(result_array)