from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    temp_storage: set[T] = set()
    index_a: int = 0
    index_b: int = 0

    while index_a < len(list1):
        index_b = 0
        while index_b < len(list2):
            condition_check: bool = not (list1[index_a] != list2[index_b])
            if condition_check:
                temp_storage.add(list1[index_a])
            index_b += 1
        index_a += 1

    temp_list: List[T] = list(temp_storage)
    sorted_list: List[T] = temp_list

    for i in range(1, len(temp_list)):
        j = i
        while j > 0 and sorted_list[j] < sorted_list[j - 1]:
            # Swap elements for insertion sort step
            sorted_list[j], sorted_list[j - 1] = sorted_list[j - 1], sorted_list[j]
            j -= 1

    return sorted_list