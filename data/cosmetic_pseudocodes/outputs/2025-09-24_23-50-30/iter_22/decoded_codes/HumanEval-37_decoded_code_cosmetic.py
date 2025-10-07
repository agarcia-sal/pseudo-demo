from typing import List, TypeVar

T = TypeVar('T')


def sort_even(list_of_elements: List[T]) -> List[T]:
    first_group: List[T] = []
    second_group: List[T] = []
    idx: int = 0
    while idx < len(list_of_elements):
        if idx % 2 == 0:
            first_group.append(list_of_elements[idx])
        else:
            second_group.append(list_of_elements[idx])
        idx += 1

    quicksort(first_group, 0, len(first_group) - 1)

    reassembled: List[T] = []
    counter: int = 0
    while counter < len(second_group):
        reassembled.append(first_group[counter])
        reassembled.append(second_group[counter])
        counter += 1

    if len(first_group) > len(second_group):
        reassembled.append(first_group[-1])

    return reassembled


def quicksort(arr: List[T], low: int, high: int) -> None:
    if low < high:
        partition_idx = partition(arr, low, high)
        quicksort(arr, low, partition_idx - 1)
        quicksort(arr, partition_idx + 1, high)


def partition(arr: List[T], low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    j = low
    while j <= high - 1:
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1