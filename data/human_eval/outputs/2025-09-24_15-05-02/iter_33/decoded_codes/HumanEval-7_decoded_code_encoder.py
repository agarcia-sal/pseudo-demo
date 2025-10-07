from typing import List

def filter_by_substring(list_of_strings: List[str], substring: str) -> List[str]:
    return [element for element in list_of_strings if substring in element]