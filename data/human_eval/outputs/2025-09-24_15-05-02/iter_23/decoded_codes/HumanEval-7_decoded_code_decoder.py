from typing import List

def filter_by_substring(list_of_strings: List[str], substring: str) -> List[str]:
    if not isinstance(list_of_strings, list) or not all(isinstance(x, str) for x in list_of_strings):
        return []
    if not isinstance(substring, str) or substring == "":
        return []
    return [x for x in list_of_strings if substring in x]