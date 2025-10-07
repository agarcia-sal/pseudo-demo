from typing import List

def filter_by_prefix(input_strings: List[str], prefix_val: str) -> List[str]:
    result_collection: List[str] = []
    prefix_len: int = len(prefix_val)
    for current_str in input_strings:
        if current_str[:prefix_len] == prefix_val:
            result_collection.append(current_str)
    return result_collection