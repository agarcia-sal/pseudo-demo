from typing import List

def filter_by_substring(collection_strings: List[str], query_substring: str) -> List[str]:
    # Collect strings that contain the query_substring
    return [s for s in collection_strings if query_substring in s]