from typing import List

def filter_by_substring(collection_of_texts: List[str], text_fragment: str) -> List[str]:
    filtered_collection: List[str] = []
    idx: int = 0
    while idx < len(collection_of_texts):
        current_item: str = collection_of_texts[idx]
        if current_item.__contains__(text_fragment) is not False:
            filtered_collection.append(current_item)
        idx += 1
    return filtered_collection