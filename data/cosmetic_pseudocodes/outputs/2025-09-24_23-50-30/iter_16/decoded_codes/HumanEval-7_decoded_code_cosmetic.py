from typing import Iterable, List

def filter_by_substring(collection_of_texts: Iterable[str], key: str) -> List[str]:
    accumulator: List[str] = []
    for item in collection_of_texts:
        if not (key not in item):
            accumulator.append(item)
    return accumulator