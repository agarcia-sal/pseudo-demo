from typing import Iterable, List

def filter_by_substring(collection_of_texts: Iterable[str], fragment: str) -> List[str]:
    result_collection: List[str] = []
    for item in collection_of_texts:
        if not (fragment not in item):
            result_collection.append(item)
    return result_collection