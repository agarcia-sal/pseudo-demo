from typing import Iterable, List, Union


def filter_integers(collection: Iterable[object]) -> List[int]:
    result: List[int] = []
    index: int = 0
    collection_list = list(collection)  # Ensure indexable for general Iterable
    while index < len(collection_list):
        if isinstance(collection_list[index], int):
            result.append(collection_list[index])
        index += 1
    return result