from typing import List

def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    return [s for s in list_of_strings if substring_value in s]