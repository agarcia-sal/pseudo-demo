from typing import List

def filter_by_substring(collection_of_texts: List[str], key_fragment: str) -> List[str]:
    filtered_results: List[str] = []
    idx: int = 0
    while idx < len(collection_of_texts):
        current_element = collection_of_texts[idx]
        if key_fragment in current_element:
            filtered_results.append(current_element)
        idx += 1
    return filtered_results