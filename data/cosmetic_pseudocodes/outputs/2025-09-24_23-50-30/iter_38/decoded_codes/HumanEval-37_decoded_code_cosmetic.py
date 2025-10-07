from typing import List, TypeVar

T = TypeVar('T')

def sort_even(stream_of_items: List[T]) -> List[T]:
    first_group: List[T] = []
    second_group: List[T] = []
    for index in range(len(stream_of_items)):
        if index % 2 == 0:
            first_group.append(stream_of_items[index])
        else:
            second_group.append(stream_of_items[index])

    sorted_first_group = sorted(first_group)  # sorted() returns a new sorted list

    merged_result: List[T] = []
    idx = 0
    while idx < len(second_group):
        merged_result.extend([sorted_first_group[idx], second_group[idx]])
        idx += 1

    if len(sorted_first_group) > len(second_group):
        merged_result.append(sorted_first_group[-1])

    return merged_result