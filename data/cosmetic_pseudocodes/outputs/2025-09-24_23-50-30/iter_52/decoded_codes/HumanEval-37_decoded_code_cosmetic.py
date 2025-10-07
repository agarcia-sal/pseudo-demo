from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    P: List[T] = []
    Q: List[T] = []

    def extract_elements_at_step(start_index: int, source_list: List[T], result: List[T], index: int) -> None:
        if index >= len(source_list):
            return
        result.append(source_list[index])
        extract_elements_at_step(start_index, source_list, result, index + 2)

    extract_elements_at_step(0, list_of_elements, P, 0)
    extract_elements_at_step(1, list_of_elements, Q, 1)

    def bubble_sort(arr: List[T], n: int) -> None:
        if n <= 1:
            return
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        bubble_sort(arr, n - 1)

    bubble_sort(P, len(P))

    R: List[T] = []

    def zip_and_extend(list1: List[T], list2: List[T], target: List[T], index: int) -> None:
        if index >= len(list2):
            return
        target.append(list1[index])
        target.append(list2[index])
        zip_and_extend(list1, list2, target, index + 1)

    zip_and_extend(P, Q, R, 0)

    if len(P) > len(Q):
        R.append(P[-1])

    return R