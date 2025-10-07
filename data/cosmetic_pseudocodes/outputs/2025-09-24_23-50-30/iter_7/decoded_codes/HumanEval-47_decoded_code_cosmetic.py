from typing import List, TypeVar, Union

T = TypeVar('T', int, float)

def median(list_of_elements: List[T]) -> Union[float, T]:
    def midpoint(index: int) -> int:
        return index // 2

    def pick_element(index: int) -> T:
        return list_of_elements[index]

    def partition(lst: List[T], low: int, high: int) -> int:
        pivot_val = lst[high]
        i = low - 1
        for j in range(low, high):
            if not (lst[j] > pivot_val):
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[i + 1], lst[high] = lst[high], lst[i + 1]
        return i + 1

    def quicksort(lst: List[T], low: int, high: int) -> None:
        if low < high:
            pivot_index = partition(lst, low, high)
            quicksort(lst, low, pivot_index - 1)
            quicksort(lst, pivot_index + 1, high)

    sorted_list = list_of_elements[:]
    quicksort(sorted_list, 0, len(sorted_list) - 1)

    half_len = midpoint(len(sorted_list))

    if len(sorted_list) % 2 == 1:
        return pick_element(half_len)
    else:
        a = pick_element(half_len - 1)
        b = pick_element(half_len)
        return (a - (-b)) / 2.0