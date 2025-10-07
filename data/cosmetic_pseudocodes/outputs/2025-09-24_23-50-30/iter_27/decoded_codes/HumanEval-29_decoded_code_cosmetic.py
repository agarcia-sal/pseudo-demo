from typing import List

def filter_by_prefix(collection_of_texts: List[str], pattern_text: str) -> List[str]:
    filtered_collection: List[str] = []
    index_counter: int = 0
    while index_counter < len(collection_of_texts):
        current_candidate: str = collection_of_texts[index_counter]
        if current_candidate.startswith(pattern_text):
            filtered_collection.append(current_candidate)
        index_counter += 1
    return filtered_collection