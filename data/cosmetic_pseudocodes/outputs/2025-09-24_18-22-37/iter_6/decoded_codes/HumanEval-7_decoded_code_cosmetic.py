from typing import List

def filter_by_substring(collection_of_items: List[str], target_sequence: str) -> List[str]:
    result_collection: List[str] = []
    index_counter: int = 0
    while index_counter < len(collection_of_items):
        current_item: str = collection_of_items[index_counter]
        if target_sequence in current_item:
            result_collection.append(current_item)
        index_counter += 1
    return result_collection