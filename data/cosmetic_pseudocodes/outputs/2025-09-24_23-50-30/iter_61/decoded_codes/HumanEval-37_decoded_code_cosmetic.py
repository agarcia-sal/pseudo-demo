from typing import List, TypeVar

T = TypeVar('T')


def bubble_sort(arr: List[T]) -> None:
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def sort_even(list_of_elements: List[T]) -> List[T]:
    def recursive_merge(
        even_list: List[T], odd_list: List[T], accumulator: List[T], position: int
    ) -> List[T]:
        min_len = min(len(even_list), len(odd_list))
        if 0 <= position < min_len:
            accumulator.append(even_list[position])
            accumulator.append(odd_list[position])
            return recursive_merge(even_list, odd_list, accumulator, position + 1)
        if position == min_len:
            if len(even_list) > len(odd_list):
                accumulator.append(even_list[position])
            return accumulator
        return accumulator  # fallback, should not be reached

    extracted_even: List[T] = []
    extracted_odd: List[T] = []

    index_tracker = 0
    while index_tracker < len(list_of_elements):
        extracted_even.append(list_of_elements[index_tracker])
        index_tracker += 2

    index_tracker = 1
    while index_tracker < len(list_of_elements):
        extracted_odd.append(list_of_elements[index_tracker])
        index_tracker += 2

    sorted_even = extracted_even[:]
    bubble_sort(sorted_even)

    return recursive_merge(sorted_even, extracted_odd, [], 0)