from typing import Iterable, List


def filter_by_prefix(collection_of_texts: Iterable[str], starting_text: str) -> List[str]:
    filtered_set: List[str] = []
    for text_element in collection_of_texts:
        if not text_element.startswith(starting_text):
            continue
        filtered_set.append(text_element)
    return filtered_set