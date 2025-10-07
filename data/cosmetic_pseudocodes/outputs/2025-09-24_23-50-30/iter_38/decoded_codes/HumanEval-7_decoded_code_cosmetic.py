from typing import Iterable, List

def filter_by_substring(container_of_texts: Iterable[str], key_fragment: str) -> List[str]:
    result_collection: List[str] = []
    for text_item in container_of_texts:
        if not (key_fragment not in text_item):
            result_collection.append(text_item)
    return result_collection