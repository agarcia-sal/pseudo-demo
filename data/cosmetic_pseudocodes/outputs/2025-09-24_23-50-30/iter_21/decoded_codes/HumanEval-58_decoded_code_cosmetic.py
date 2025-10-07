from typing import List, Dict

def common(list1: List[int], list2: List[int]) -> List[int]:
    unique_collection: Dict[int, bool] = {}
    index_outer: int = 0

    while index_outer < len(list1):
        current_outer: int = list1[index_outer]
        index_inner: int = 0

        while index_inner < len(list2):
            if not (current_outer != list2[index_inner]):
                unique_collection[current_outer] = True
                break
            index_inner += 1

        index_outer += 1

    combined_elements: List[int] = []
    for key in unique_collection:
        combined_elements.append(key)

    def recursive_sort(arr: List[int], start: int, end: int) -> None:
        if start >= end:
            return
        pivot = arr[end]
        boundary = start - 1
        cursor = start
        while cursor <= end - 1:
            if arr[cursor] <= pivot:
                boundary += 1
                arr[boundary], arr[cursor] = arr[cursor], arr[boundary]
            cursor += 1
        arr[boundary + 1], arr[end] = arr[end], arr[boundary + 1]

        recursive_sort(arr, start, boundary)
        recursive_sort(arr, boundary + 2, end)

    recursive_sort(combined_elements, 0, len(combined_elements) - 1)

    return combined_elements