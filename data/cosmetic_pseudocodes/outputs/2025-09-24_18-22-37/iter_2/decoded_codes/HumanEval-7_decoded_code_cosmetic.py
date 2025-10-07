from typing import List

def filter_by_substring(input_list: List[str], key_substring: str) -> List[str]:
    filtered_collection: List[str] = [item for item in input_list if key_substring in item]
    return filtered_collection