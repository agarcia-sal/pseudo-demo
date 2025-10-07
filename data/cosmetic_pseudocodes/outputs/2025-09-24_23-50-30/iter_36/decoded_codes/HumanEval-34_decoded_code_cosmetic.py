from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(collection: Iterable[T]) -> List[T]:
    temporary_container = set()
    index = 0
    collection_list = list(collection)  # To support indexing and length reliably

    while index < len(collection_list):
        temporary_container.add(collection_list[index])
        index += 1

    result_list = [element for element in temporary_container]
    result_list.sort()
    return result_list