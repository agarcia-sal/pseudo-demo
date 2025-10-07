from typing import List, TypeVar

T = TypeVar('T')

def unique(list_of_elements: List[T]) -> List[T]:
    distinct_items = set(list_of_elements)  # eliminate duplicates
    result = list(distinct_items)
    index = 1
    while index < len(result):
        inner_index = index + 1
        while inner_index <= len(result):
            if result[inner_index] < result[index]:
                result[index], result[inner_index] = result[inner_index], result[index]
            inner_index += 1
        index += 1
    return result