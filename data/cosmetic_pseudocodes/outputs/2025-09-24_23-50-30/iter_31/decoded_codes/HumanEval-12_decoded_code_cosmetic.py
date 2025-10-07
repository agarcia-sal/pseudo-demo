from typing import List, Optional

def longest(array_of_texts: List[str]) -> Optional[str]:
    if not array_of_texts:
        return None

    top_size: int = 0
    index_counter: int = 0
    while index_counter < len(array_of_texts):
        current_length = len(array_of_texts[index_counter])
        if current_length > top_size:
            top_size = current_length
        index_counter += 1

    pointer: int = 0
    while pointer < len(array_of_texts):
        if len(array_of_texts[pointer]) == top_size:
            return array_of_texts[pointer]
        pointer += 1