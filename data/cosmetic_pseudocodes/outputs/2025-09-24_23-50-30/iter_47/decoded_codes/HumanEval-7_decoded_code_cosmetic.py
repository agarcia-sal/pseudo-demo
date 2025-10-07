from typing import List

def filter_by_substring(collection_of_texts: List[str], segment: str) -> List[str]:
    result_collection: List[str] = []
    index_counter: int = 0
    while index_counter < len(collection_of_texts):
        current_text: str = collection_of_texts[index_counter]
        if segment in current_text:
            result_collection.append(current_text)
        index_counter += 1
    return result_collection