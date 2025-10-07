from typing import List

def filter_by_prefix(string_collection: List[str], pattern_text: str) -> List[str]:
    result_collection: List[str] = []
    prefix_length = len(pattern_text)
    for element_text in string_collection:
        if element_text[:prefix_length] == pattern_text:
            result_collection.append(element_text)
    return result_collection