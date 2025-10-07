from typing import List, TypeVar

T = TypeVar('T')


def sort_even(list_of_elements: List[T]) -> List[T]:
    def quicksort(arr: List[T], low: int, high: int) -> None:
        if low >= high:
            return
        pivot_val = arr[high]
        i = low - 1
        for j in range(low, high):
            if not (arr[j] > pivot_val):
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pi = i + 1
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

    def interleave(elems_A: List[T], elems_B: List[T], position: int, accumulator: List[T]) -> List[T]:
        if position == len(elems_B):
            # Add the final unmatched element from elems_A (last even index)
            return accumulator + [elems_A[position]]
        return interleave(
            elems_A,
            elems_B,
            position + 1,
            accumulator + [elems_A[position], elems_B[position]],
        )

    subset_one: List[T] = []
    idx_one = 0
    while idx_one < len(list_of_elements):
        subset_one.append(list_of_elements[idx_one])
        idx_one += 2

    subset_two: List[T] = []
    idx_two = 1
    while idx_two < len(list_of_elements):
        subset_two.append(list_of_elements[idx_two])
        idx_two += 2

    quicksort(subset_one, 0, len(subset_one) - 1)

    # Both branches actually do the same thing, but replicate logic exactly
    if len(subset_two) >= len(subset_one):
        return interleave(subset_one, subset_two, 0, [])
    return interleave(subset_one, subset_two, 0, [])