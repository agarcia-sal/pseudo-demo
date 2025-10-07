from typing import Iterable, List

def filter_by_prefix(collection_of_texts: Iterable[str], start_substring: str) -> List[str]:
    filtered_results: List[str] = []
    for text_element in collection_of_texts:
        if text_element.startswith(start_substring):
            filtered_results.append(text_element)
    return filtered_results