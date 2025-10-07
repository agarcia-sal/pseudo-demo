from typing import List

def filter_by_substring(container_of_texts: List[str], pattern: str) -> List[str]:
    index_tracker: int = 0
    matched_items: List[str] = []
    while index_tracker < len(container_of_texts):
        if pattern in container_of_texts[index_tracker]:
            matched_items.append(container_of_texts[index_tracker])
        index_tracker += 1
    return matched_items