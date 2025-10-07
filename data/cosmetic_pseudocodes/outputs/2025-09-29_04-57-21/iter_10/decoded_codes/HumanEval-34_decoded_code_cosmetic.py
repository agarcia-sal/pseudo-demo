from typing import List, TypeVar

T = TypeVar('T', bound=object)

def unique(list_of_elements: List[T]) -> List[T]:
    distinct_collection: set[T] = set()
    temp_list: List[T] = []
    for item in list_of_elements:
        distinct_collection.add(item)
    for element in distinct_collection:
        temp_list.append(element)
    temp_list.sort()
    return temp_list