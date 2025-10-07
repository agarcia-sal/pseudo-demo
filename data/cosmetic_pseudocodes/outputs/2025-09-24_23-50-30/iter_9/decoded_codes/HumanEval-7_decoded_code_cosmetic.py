from typing import Iterable, List

def filter_by_substring(input_collection: Iterable[str], key_fragment: str) -> List[str]:
    result_collection: List[str] = []
    for element in input_collection:
        if not (key_fragment not in element):
            result_collection.append(element)
    return result_collection