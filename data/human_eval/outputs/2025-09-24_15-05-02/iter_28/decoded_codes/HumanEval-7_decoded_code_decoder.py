from typing import List


def filter_by_substring(list_of_strings: List[str], substring: str) -> List[str]:
    return [string for string in list_of_strings if substring in string]