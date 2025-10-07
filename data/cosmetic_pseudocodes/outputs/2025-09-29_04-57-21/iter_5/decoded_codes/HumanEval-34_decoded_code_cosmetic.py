from typing import List, TypeVar

T = TypeVar('T')

def unique(list_of_elements: List[T]) -> List[T]:
    temp_set = set()
    for element in list_of_elements:
        temp_set.add(element)
    result_list = [item for item in temp_set]
    index = 1
    length = len(result_list)
    while index < length:
        j = index + 1
        while j <= length and result_list[j - 1] < result_list[index - 1]:
            result_list[index - 1], result_list[j - 1] = result_list[j - 1], result_list[index - 1]
            j += 1
        index += 1
    return result_list