from typing import Iterable, List

def filter_by_substring(collection_of_texts: Iterable[str], target_substring: str) -> List[str]:
    accumulator: List[str] = []
    for element in collection_of_texts:
        if target_substring in element:
            accumulator.append(element)
    return accumulator