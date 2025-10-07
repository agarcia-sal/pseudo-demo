from typing import List

def sorted_list_sum(words_collection: List[str]) -> List[str]:
    words_collection_sorted: List[str] = sorted(words_collection)
    filtered_collection: List[str] = []
    index: int = 0
    while index < len(words_collection_sorted):
        current_word: str = words_collection_sorted[index]
        if (len(current_word) % 2) == 0:
            filtered_collection.append(current_word)
        index += 1
    return sorted(filtered_collection, key=len)