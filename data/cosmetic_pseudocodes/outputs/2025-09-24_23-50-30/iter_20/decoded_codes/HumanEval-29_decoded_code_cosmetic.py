from typing import Iterable, List

def filter_by_prefix(collection_of_words: Iterable[str], starting_sequence: str) -> List[str]:
    result_collection: List[str] = []
    for element in collection_of_words:
        if not element.startswith(starting_sequence):
            continue
        result_collection.append(element)
    return result_collection