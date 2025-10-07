from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    temp_a: List[T] = []
    temp_b: List[T] = []
    for idx in range(len(list_of_elements)):
        if idx % 2 == 0:
            temp_a.append(list_of_elements[idx])
        else:
            temp_b.append(list_of_elements[idx])
    temp_a.sort()
    result_list: List[T] = []
    pos = 0
    while pos < len(temp_b):
        result_list.append(temp_a[pos])
        result_list.append(temp_b[pos])
        pos += 1
    if len(temp_a) > len(temp_b):
        result_list.append(temp_a[-1])
    return result_list