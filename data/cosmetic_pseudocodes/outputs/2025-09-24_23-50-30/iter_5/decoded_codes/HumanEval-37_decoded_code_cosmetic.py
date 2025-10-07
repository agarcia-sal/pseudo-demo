from typing import List, TypeVar

T = TypeVar('T')


def sort_even(list_of_elements: List[T]) -> List[T]:
    first_group: List[T] = []
    second_group: List[T] = []
    for idx in range(len(list_of_elements)):
        if idx % 2 == 0:
            first_group.append(list_of_elements[idx])
        else:
            second_group.append(list_of_elements[idx])
    sorted_first = sorted(first_group)
    combined: List[T] = []
    i = 0
    while i < len(second_group):
        combined.append(sorted_first[i])
        combined.append(second_group[i])
        i += 1
    if len(sorted_first) > len(second_group):
        combined.append(sorted_first[-1])
    return combined