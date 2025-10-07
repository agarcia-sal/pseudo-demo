from typing import List

def filter_by_prefix(vector_of_strings: List[str], string_prefix: str) -> List[str]:
    result_collection: List[str] = []
    position: int = 0
    prefix_len: int = len(string_prefix)
    while position < len(vector_of_strings):
        current_element: str = vector_of_strings[position]
        if current_element[:prefix_len] == string_prefix:
            result_collection.append(current_element)
        position += 1
    return result_collection