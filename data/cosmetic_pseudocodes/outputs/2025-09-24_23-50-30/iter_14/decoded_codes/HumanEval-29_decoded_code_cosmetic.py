from typing import Iterable, List

def filter_by_prefix(collection_of_texts: Iterable[str], start_sequence: str) -> List[str]:
    accumulated: List[str] = []
    for element in collection_of_texts:
        if not element.startswith(start_sequence):
            continue
        accumulated.append(element)
    return accumulated