from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    filtered_strings: List[str] = []
    for x in strings:
        if x.startswith(prefix):
            filtered_strings.append(x)
    return filtered_strings