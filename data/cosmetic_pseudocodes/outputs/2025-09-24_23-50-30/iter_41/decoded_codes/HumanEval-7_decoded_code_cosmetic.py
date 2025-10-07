from typing import List

def filter_by_substring(array_strings: List[str], pattern_value: str) -> List[str]:
    result_collection: List[str] = []
    idx: int = 0
    while idx < len(array_strings):
        current_element: str = array_strings[idx]
        if pattern_value in current_element:
            result_collection.append(current_element)
        idx += 1
    return result_collection