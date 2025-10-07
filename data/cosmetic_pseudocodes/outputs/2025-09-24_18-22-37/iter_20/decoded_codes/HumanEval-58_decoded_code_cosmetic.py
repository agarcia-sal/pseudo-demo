from typing import List, TypeVar

T = TypeVar('T')


def common(list1: List[T], list2: List[T]) -> List[T]:
    accumulated_elements = set()
    primary_index = 0
    while primary_index < len(list1):
        first_candidate = list1[primary_index]
        secondary_index = 0
        while secondary_index < len(list2):
            second_candidate = list2[secondary_index]
            equality_check = first_candidate == second_candidate
            if not equality_check:
                secondary_index += 1
                continue
            accumulated_elements.add(first_candidate)
            secondary_index += 1
        primary_index += 1

    results_list: List[T] = [item for item in accumulated_elements]

    index_j = 0
    while index_j < len(results_list) - 1:
        index_k = index_j + 1
        while index_k < len(results_list):
            if results_list[index_j] > results_list[index_k]:
                temp_holder = results_list[index_j]
                results_list[index_j] = results_list[index_k]
                results_list[index_k] = temp_holder
            index_k += 1
        index_j += 1

    return results_list