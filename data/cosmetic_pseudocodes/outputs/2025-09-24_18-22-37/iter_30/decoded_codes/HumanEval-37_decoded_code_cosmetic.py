from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    filtered_a: List[T] = []
    filtered_b: List[T] = []

    idx_a = 0
    while idx_a < len(list_of_elements):
        filtered_a.append(list_of_elements[idx_a])
        idx_a += 2

    idx_b = 1
    while idx_b < len(list_of_elements):
        filtered_b.append(list_of_elements[idx_b])
        idx_b += 2

    filtered_a.sort()

    merged_result: List[T] = []
    pointer_a = 0
    pointer_b = 0
    while pointer_a < len(filtered_a) and pointer_b < len(filtered_b):
        merged_result.append(filtered_a[pointer_a])
        merged_result.append(filtered_b[pointer_b])
        pointer_a += 1
        pointer_b += 1

    if len(filtered_a) > len(filtered_b):  # Handle odd length case
        merged_result.append(filtered_a[-1])

    return merged_result