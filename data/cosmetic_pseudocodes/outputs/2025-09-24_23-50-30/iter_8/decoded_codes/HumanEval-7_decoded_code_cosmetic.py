from typing import List

def filter_by_substring(array_input: List[str], sequence_key: str) -> List[str]:
    result_collection: List[str] = []
    for current_candidate in array_input:
        if sequence_key in current_candidate:
            result_collection.append(current_candidate)
    return result_collection