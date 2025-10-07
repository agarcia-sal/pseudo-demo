from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    first_subset: List[T] = []
    second_subset: List[T] = []
    position_counter: int = 0

    while position_counter < len(list_of_elements):
        if position_counter % 2 == 0:
            first_subset.append(list_of_elements[position_counter])
        else:
            second_subset.append(list_of_elements[position_counter])
        position_counter += 1

    first_subset.sort()
    result_container: List[T] = []

    def insert_pairs(index: int) -> None:
        if index == len(second_subset):
            return
        result_container.append(first_subset[index])
        result_container.append(second_subset[index])
        insert_pairs(index + 1)

    insert_pairs(0)

    if len(first_subset) - len(second_subset) > 0:
        result_container.append(first_subset[-1])

    return result_container