from typing import Iterable, List

def filter_by_prefix(strings_collection: Iterable[str], prefix_key: str) -> List[str]:
    filtered_results: List[str] = []
    prefix_len: int = len(prefix_key)
    for element in strings_collection:
        if element[:prefix_len] == prefix_key:
            filtered_results.append(element)
    return filtered_results