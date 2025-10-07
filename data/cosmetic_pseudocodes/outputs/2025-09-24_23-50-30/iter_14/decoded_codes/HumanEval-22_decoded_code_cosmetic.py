from typing import Iterable, List, Union

def filter_integers(collection: Iterable[object]) -> List[int]:
    filtered_results: List[int] = []
    index: int = 0
    collection_list = list(collection)
    while index < len(collection_list):
        item = collection_list[index]
        if isinstance(item, int):
            filtered_results.append(item)
        index += 1
    return filtered_results