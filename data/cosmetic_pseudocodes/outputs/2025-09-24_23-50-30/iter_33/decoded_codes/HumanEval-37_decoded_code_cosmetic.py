from typing import List, TypeVar

T = TypeVar('T')

def bubble_sort(arr: List[T]) -> None:
    n: int = len(arr)
    outer: int = 0
    while outer < n - 1:
        inner: int = 0
        while inner < n - outer - 1:
            if arr[inner] > arr[inner + 1]:
                arr[inner], arr[inner + 1] = arr[inner + 1], arr[inner]
            inner += 1
        outer += 1

def sort_even(list_of_elements: List[T]) -> List[T]:
    accumulator: List[T] = []
    first_subset: List[T] = []
    second_subset: List[T] = []
    index_counter: int = 0

    while index_counter < len(list_of_elements):
        if index_counter % 2 == 0:
            first_subset.append(list_of_elements[index_counter])
        else:
            second_subset.append(list_of_elements[index_counter])
        index_counter += 1

    bubble_sort(first_subset)

    def merge(list_a: List[T], list_b: List[T], position_a: int, position_b: int) -> None:
        if position_a >= len(list_a):
            if position_b >= len(list_b):
                return
            accumulator.append(list_b[position_b])
            merge(list_a, list_b, position_a, position_b + 1)
        elif position_b >= len(list_b):
            accumulator.append(list_a[position_a])
            merge(list_a, list_b, position_a + 1, position_b)
        else:
            accumulator.append(list_a[position_a])
            accumulator.append(list_b[position_b])
            merge(list_a, list_b, position_a + 1, position_b + 1)

    merge(first_subset, second_subset, 0, 0)

    return accumulator