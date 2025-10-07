from typing import List, TypeVar

T = TypeVar('T')

def unique(list_of_elements: List[T]) -> List[T]:
    temp_collection: dict[T, bool] = {}
    index: int = 0
    while index < len(list_of_elements):
        current_item = list_of_elements[index]
        if current_item not in temp_collection:
            temp_collection[current_item] = True
        index += 1
    result_list: List[T] = list(temp_collection.keys())
    result_list.sort()
    return result_list