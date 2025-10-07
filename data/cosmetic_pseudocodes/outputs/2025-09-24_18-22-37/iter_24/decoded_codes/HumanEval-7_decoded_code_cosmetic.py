from typing import List


def filter_by_substring(array_of_texts: List[str], text_snippet: str) -> List[str]:
    filtered_collection: List[str] = []
    index_counter: int = 0
    collection_size: int = len(array_of_texts)
    while index_counter < collection_size:
        current_string: str = array_of_texts[index_counter]
        if text_snippet in current_string:
            filtered_collection.append(current_string)
        index_counter += 1
    return filtered_collection