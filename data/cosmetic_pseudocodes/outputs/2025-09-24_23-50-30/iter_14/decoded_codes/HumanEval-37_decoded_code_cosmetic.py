from typing import List, TypeVar

T = TypeVar('T', bound=object)

def sort_even(list_of_elements: List[T]) -> List[T]:
    first_set: List[T] = []
    second_set: List[T] = []
    for index in range(len(list_of_elements)):
        if index % 2 == 0:
            first_set.append(list_of_elements[index])
        else:
            second_set.append(list_of_elements[index])
    first_set.sort()
    result_list: List[T] = []
    counter: int = 0
    while counter < len(second_set):
        result_list.append(first_set[counter])
        result_list.append(second_set[counter])
        counter += 1
    if len(first_set) > len(second_set):
        result_list.append(first_set[-1])
    return result_list