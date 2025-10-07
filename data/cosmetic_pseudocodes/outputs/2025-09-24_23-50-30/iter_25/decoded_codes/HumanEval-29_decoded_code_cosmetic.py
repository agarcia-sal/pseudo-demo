from typing import Iterable, List

def filter_by_prefix(collection_of_texts: Iterable[str], starting_substring: str) -> List[str]:
    filtered_collection: List[str] = [
        text_element for text_element in collection_of_texts
        if text_element.startswith(starting_substring)
    ]
    return filtered_collection