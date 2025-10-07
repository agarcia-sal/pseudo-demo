from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(collection: Iterable[T]) -> List[T]:
    temp_set = set()
    index = 0
    collection_list = list(collection)
    while index < len(collection_list):
        element = collection_list[index]
        temp_set.add(element)
        index += 1
    temp_list = []
    for each_item in temp_set:
        temp_list.append(each_item)
    temp_list.sort()
    return temp_list