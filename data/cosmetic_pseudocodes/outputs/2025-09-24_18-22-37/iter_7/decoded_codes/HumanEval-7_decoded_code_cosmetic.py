from typing import List

def filter_by_substring(collection_of_texts: List[str], target_sequence: str) -> List[str]:
    filtered_collection: List[str] = []
    index_counter: int = 0
    while index_counter < len(collection_of_texts):
        current_text: str = collection_of_texts[index_counter]
        if current_text.find(target_sequence) != -1:
            filtered_collection.append(current_text)
        index_counter += 1
    return filtered_collection