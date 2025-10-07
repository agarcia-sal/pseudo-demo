from typing import List, Optional, Dict

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    temp_map: Dict[int, bool] = {}
    for index in range(len(list_of_integers)):
        temp_map[list_of_integers[index]] = True

    unique_elements: List[int] = [key for key in temp_map]

    def quick_sort(arr: List[int], low: int, high: int) -> None:
        if low >= high:
            return
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pivot_index = i + 1
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

    quick_sort(unique_elements, 0, len(unique_elements) - 1)

    if len(unique_elements) < 2:
        return None
    return unique_elements[1]