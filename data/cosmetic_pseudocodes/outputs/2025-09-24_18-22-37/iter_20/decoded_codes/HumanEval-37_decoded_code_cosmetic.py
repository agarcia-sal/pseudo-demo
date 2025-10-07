from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    step_value: int = 2
    start_zero: int = 0
    first_subset: List[T] = []
    second_subset: List[T] = []

    idx_a: int = start_zero
    while idx_a < len(list_of_elements):
        first_subset.append(list_of_elements[idx_a])
        idx_a += step_value

    idx_b: int = start_zero + 1
    while idx_b < len(list_of_elements):
        second_subset.append(list_of_elements[idx_b])
        idx_b += step_value

    # Bubble sort first_subset in non-decreasing order
    n: int = len(first_subset)
    outer_counter: int = n - 1
    while outer_counter > 0:
        inner_counter: int = 0
        while inner_counter < outer_counter:
            if first_subset[inner_counter] > first_subset[inner_counter + 1]:
                # Swap elements
                temp_var = first_subset[inner_counter]
                first_subset[inner_counter] = first_subset[inner_counter + 1]
                first_subset[inner_counter + 1] = temp_var
            inner_counter += 1
        outer_counter -= 1

    merged_list: List[T] = []
    iter_a: int = 0
    len_first: int = len(first_subset)
    len_second: int = len(second_subset)

    while iter_a < len_second:
        merged_pair: List[T] = [first_subset[iter_a], second_subset[iter_a]]
        append_idx: int = 0
        while append_idx < len(merged_pair):
            merged_list.append(merged_pair[append_idx])
            append_idx += 1
        iter_a += 1

    if len_first > len_second:
        merged_list.append(first_subset[len_first - 1])

    return merged_list