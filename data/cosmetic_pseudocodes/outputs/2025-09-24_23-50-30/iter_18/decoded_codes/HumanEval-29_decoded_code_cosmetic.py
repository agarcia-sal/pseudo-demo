from typing import List

def filter_by_prefix(queue_of_texts: List[str], match_prefix: str) -> List[str]:
    result_collection: List[str] = []
    index_tracker: int = 0
    while index_tracker < len(queue_of_texts):
        element_candidate: str = queue_of_texts[index_tracker]
        if not match_prefix or element_candidate[:len(match_prefix)] == match_prefix:
            result_collection.append(element_candidate)
        index_tracker += 1
    return result_collection