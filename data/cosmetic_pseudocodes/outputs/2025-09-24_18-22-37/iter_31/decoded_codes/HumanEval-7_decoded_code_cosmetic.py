from typing import List

def filter_by_substring(source_strings: List[str], pattern: str) -> List[str]:
    return [candidate for candidate in source_strings if pattern in candidate]