from typing import List

def filter_by_substring(collection_of_strings: List[str], needle: str) -> List[str]:
    filtered_collection: List[str] = []
    index_counter: int = 0
    while True:
        if index_counter >= len(collection_of_strings):
            break
        current_item: str = collection_of_strings[index_counter]
        if needle in current_item:
            filtered_collection.append(current_item)
        index_counter += 1
    return filtered_collection