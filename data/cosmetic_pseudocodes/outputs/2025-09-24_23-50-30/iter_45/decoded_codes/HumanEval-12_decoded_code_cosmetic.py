from typing import List, Optional

def longest(collection_of_texts: List[str]) -> Optional[str]:
    if not collection_of_texts:
        return None

    peak_size: int = float('-inf')
    index_counter: int = 0
    while index_counter < len(collection_of_texts):
        temp_size: int = len(collection_of_texts[index_counter])
        if temp_size > peak_size:
            peak_size = temp_size
        index_counter += 1

    pointer: int = 0
    while pointer < len(collection_of_texts):
        if len(collection_of_texts[pointer]) == peak_size:
            return collection_of_texts[pointer]
        pointer += 1

    return None  # In case all elements are empty or no max found