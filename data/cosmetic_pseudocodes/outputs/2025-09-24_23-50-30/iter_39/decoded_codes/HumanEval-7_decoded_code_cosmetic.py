from typing import List

def filter_by_substring(aggregate_strings: List[str], pattern_substring: str) -> List[str]:
    result_collection: List[str] = []
    index: int = 0
    while index < len(aggregate_strings):
        if pattern_substring in aggregate_strings[index]:
            result_collection.append(aggregate_strings[index])
        index += 1
    return result_collection