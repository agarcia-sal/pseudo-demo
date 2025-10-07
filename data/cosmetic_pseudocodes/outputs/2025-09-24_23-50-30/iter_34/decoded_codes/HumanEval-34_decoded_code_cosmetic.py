from typing import Iterable, List, TypeVar

T = TypeVar('T', bound=object)

def unique(collection: Iterable[T]) -> List[T]:
    temp_map: dict[T, bool] = {}
    idx = 0
    collection_list = list(collection)  # To support indexing reliably
    while idx < len(collection_list):
        temp_map[collection_list[idx]] = True
        idx += 1
    result_list = [key for key in temp_map.keys()]
    return sorted(result_list)