from typing import List

def filter_by_prefix(array_of_texts: List[str], key_text: str) -> List[str]:
    filtered_collection: List[str] = []
    index_counter: int = 0
    while index_counter < len(array_of_texts):
        if array_of_texts[index_counter].startswith(key_text):
            filtered_collection.append(array_of_texts[index_counter])
        index_counter += 1
    return filtered_collection