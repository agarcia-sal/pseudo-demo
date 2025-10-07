from typing import List

def sort_even(elements_list: List[int]) -> List[int]:
    def extract_indices(src_list: List[int], start_idx: int, acc: List[int]) -> List[int]:
        if start_idx >= len(src_list):
            return acc
        return extract_indices(src_list, start_idx + 2, acc + [src_list[start_idx]])

    evens: List[int] = extract_indices(elements_list, 0, [])
    odds: List[int] = extract_indices(elements_list, 1, [])

    def insertion_sort(arr: List[int], i: int) -> List[int]:
        if i >= len(arr):
            return arr
        key = arr[i]

        def insert_pos(j: int) -> List[int]:
            if j < 0 or arr[j] <= key:
                # Rebuild arr with key inserted at correct position
                return arr[:j+1] + [key] + arr[j+1:i] + arr[i+1:]
            return insert_pos(j - 1)

        arr = insert_pos(i - 1)
        return insertion_sort(arr, i + 1)

    sorted_evens: List[int] = insertion_sort(evens, 1)

    def interleave_lists(list_a: List[int], list_b: List[int], acc: List[int], idx: int) -> List[int]:
        if idx >= len(list_b):
            return acc
        return interleave_lists(list_a, list_b, acc + [list_a[idx], list_b[idx]], idx + 1)

    merged: List[int] = interleave_lists(sorted_evens, odds, [], 0)

    if len(sorted_evens) - len(odds) > 0:
        merged.append(sorted_evens[-1])

    return merged