from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    first_group: List[T] = []
    second_group: List[T] = []
    for index in range(len(list_of_elements)):
        if index % 2 == 0:
            first_group.append(list_of_elements[index])
        else:
            second_group.append(list_of_elements[index])
    first_group.sort()
    final_list: List[T] = []
    counter = 0
    while counter < len(second_group):
        final_list.append(first_group[counter])
        final_list.append(second_group[counter])
        counter += 1
    if len(first_group) > len(second_group):
        final_list.append(first_group[-1])
    return final_list