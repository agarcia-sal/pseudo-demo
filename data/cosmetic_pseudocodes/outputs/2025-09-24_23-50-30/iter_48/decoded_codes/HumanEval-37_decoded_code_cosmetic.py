from typing import List, Sequence

def procedure_sort(target_collection: List[int], ascending: bool) -> None:
    swapped_flag = True
    while swapped_flag:
        swapped_flag = False
        i = 1
        while i < len(target_collection):
            if ascending and target_collection[i - 1] > target_collection[i]:
                target_collection[i - 1], target_collection[i] = target_collection[i], target_collection[i - 1]
                swapped_flag = True
            i += 1

def sort_even(numeric_sequence: Sequence[int]) -> List[int]:
    first_subset: List[int] = []
    second_subset: List[int] = []
    index_pointer = 0
    while index_pointer < len(numeric_sequence):
        if not (index_pointer % 2 != 0):
            first_subset.append(numeric_sequence[index_pointer])
        else:
            second_subset.append(numeric_sequence[index_pointer])
        index_pointer += 1

    procedure_sort(first_subset, True)
    result_sequence: List[int] = []
    position_counter = 0
    while position_counter < len(second_subset):
        result_sequence.append(first_subset[position_counter])
        result_sequence.append(second_subset[position_counter])
        position_counter += 1

    if not (len(second_subset) >= len(first_subset)):
        result_sequence.append(first_subset[-1])
    return result_sequence