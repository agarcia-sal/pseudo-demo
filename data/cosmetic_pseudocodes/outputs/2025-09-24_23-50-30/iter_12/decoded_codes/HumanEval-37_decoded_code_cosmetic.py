from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    temp_even: List[T] = []
    temp_odd: List[T] = []
    index_counter: int = 0

    while index_counter < len(list_of_elements):
        if index_counter % 2 == 0:
            temp_even.append(list_of_elements[index_counter])
        else:
            temp_odd.append(list_of_elements[index_counter])
        index_counter += 1

    sorted_even: List[T] = temp_even[:]  # copy to avoid modifying original even list
    i: int = 0
    while i < len(sorted_even) - 1:
        j: int = i + 1
        while j < len(sorted_even):
            if sorted_even[i] > sorted_even[j]:
                sorted_even[i], sorted_even[j] = sorted_even[j], sorted_even[i]
            j += 1
        i += 1

    result_arr: List[T] = []
    pos: int = 0
    while pos < len(temp_odd):
        result_arr.append(sorted_even[pos])
        result_arr.append(temp_odd[pos])
        pos += 1

    if len(sorted_even) > len(temp_odd):
        result_arr.append(sorted_even[-1])

    return result_arr