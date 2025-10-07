from typing import List

def filter_by_substring(collection_of_texts: List[str], target_substring: str) -> List[str]:
    filtered_collection: List[str] = []
    index_counter: int = 0
    while index_counter < len(collection_of_texts):
        current_text = collection_of_texts[index_counter]
        if target_substring in current_text:
            filtered_collection.append(current_text)
        index_counter += 1
    return filtered_collection