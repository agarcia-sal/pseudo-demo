from typing import List

def filter_by_prefix(collection_of_texts: List[str], starter_sequence: str) -> List[str]:
    result_collection: List[str] = []

    def helper(iterator_index: int) -> None:
        if iterator_index >= len(collection_of_texts):
            return
        current_item = collection_of_texts[iterator_index]
        if current_item.startswith(starter_sequence):
            result_collection.append(current_item)
        helper(iterator_index + 1)

    helper(0)
    return result_collection