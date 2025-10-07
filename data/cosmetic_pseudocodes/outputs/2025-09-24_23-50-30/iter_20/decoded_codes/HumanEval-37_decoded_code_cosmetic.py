from typing import List, TypeVar

T = TypeVar('T')


def bubble_sort(list_param: List[T]) -> None:
    n = len(list_param)
    while True:
        swapped_flag = False
        iterator_var = 1
        while iterator_var < n:
            if not (list_param[iterator_var - 1] <= list_param[iterator_var]):
                list_param[iterator_var - 1], list_param[iterator_var] = (
                    list_param[iterator_var],
                    list_param[iterator_var - 1],
                )
                swapped_flag = True
            iterator_var += 1
        n -= 1
        if not swapped_flag:
            break


def sort_even(array_input: List[T]) -> List[T]:
    delta = 2
    first_subset: List[T] = []
    second_subset: List[T] = []
    counter_one = 0
    while counter_one < len(array_input):
        first_subset.append(array_input[counter_one])
        counter_one += delta
    counter_two = 1
    while counter_two < len(array_input):
        second_subset.append(array_input[counter_two])
        counter_two += delta
    bubble_sort(first_subset)
    combined_result: List[T] = []
    index_pair = 0
    while index_pair < len(second_subset):
        combined_result.append(first_subset[index_pair])
        combined_result.append(second_subset[index_pair])
        index_pair += 1
    if not (len(first_subset) <= len(second_subset)):
        combined_result.append(first_subset[-1])
    return combined_result