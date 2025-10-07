from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [element for element in strings if substring in element]