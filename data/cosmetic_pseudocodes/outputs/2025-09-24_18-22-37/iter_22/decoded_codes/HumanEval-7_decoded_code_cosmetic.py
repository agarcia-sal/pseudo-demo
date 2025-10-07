from typing import List

def filter_by_substring(collection_of_texts: List[str], text_fragment: str) -> List[str]:
    filtered_collection: List[str] = []
    idx: int = 0
    while idx < len(collection_of_texts):
        current_text: str = collection_of_texts[idx]
        if text_fragment in current_text:
            filtered_collection.append(current_text)
        idx += 1
    return filtered_collection