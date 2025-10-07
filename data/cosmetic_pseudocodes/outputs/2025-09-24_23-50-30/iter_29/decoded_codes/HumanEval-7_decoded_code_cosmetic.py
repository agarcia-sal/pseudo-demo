from typing import List

def filter_by_substring(sequence_elements: List[str], key_fragment: str) -> List[str]:
    filtered: List[str] = []
    for item in sequence_elements:
        if not (key_fragment not in item):
            filtered.append(item)
    return filtered