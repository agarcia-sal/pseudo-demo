from typing import List

def filter_by_substring(list_of_strings: List[str], substring_to_find: str) -> List[str]:
    return [s for s in list_of_strings if substring_to_find in s]