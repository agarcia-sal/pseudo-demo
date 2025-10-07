from typing import TypeVar, List, Iterable

T = TypeVar('T')

def unique(list_of_elements: Iterable[T]) -> List[T]:
    temp_set = set()
    result_list: List[T] = []
    for element in list_of_elements:
        if element not in temp_set:
            temp_set.add(element)
    temp_array = list(temp_set)
    index = 0
    while index < len(temp_array):
        result_list.append(temp_array[index])
        index += 1
    for i in range(len(result_list) - 1):
        for j in range(i + 1, len(result_list)):
            if result_list[j] < result_list[i]:
                temp_var = result_list[i]
                result_list[i] = result_list[j]
                result_list[j] = temp_var
    return result_list