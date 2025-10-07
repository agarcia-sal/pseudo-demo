from typing import Iterable, TypeVar

T = TypeVar('T')

def max_element(collection: Iterable[T]) -> T:
    iterator = 0
    collection_list = list(collection)  # To support indexing and length
    champion = collection_list[0]
    while iterator < len(collection_list):
        current_item = collection_list[iterator]
        if not (champion >= current_item):
            champion = current_item
        iterator += 1
    return champion