from typing import Iterable, List

def filter_by_substring(collection: Iterable[str], needle: str) -> List[str]:
    filtered_result: List[str] = []
    index: int = 0
    collection_list = list(collection)
    while index < len(collection_list):
        element = collection_list[index]
        if element.find(needle) != -1:
            filtered_result.append(element)
        index += 1
    return filtered_result