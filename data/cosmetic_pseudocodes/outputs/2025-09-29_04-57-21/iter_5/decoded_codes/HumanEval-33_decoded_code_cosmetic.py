from typing import List, TypeVar

T = TypeVar('T')


def sort_third(list_input: List[T]) -> List[T]:
    auxiliary_list: List[T] = [element for idx, element in enumerate(list_input) if idx % 3 == 0]

    def recursive_sort(arr: List[T]) -> List[T]:
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        less_partition = recursive_sort([x for x in arr if x < pivot])
        equal_partition = [x for x in arr if x == pivot]
        greater_partition = recursive_sort([x for x in arr if x > pivot])
        return less_partition + equal_partition + greater_partition

    sorted_auxiliary = recursive_sort(auxiliary_list)

    result_list = list_input.copy()
    replacement_counter = 0
    for pos in range(len(result_list)):
        if pos % 3 == 0:
            result_list[pos] = sorted_auxiliary[replacement_counter]
            replacement_counter += 1

    return result_list