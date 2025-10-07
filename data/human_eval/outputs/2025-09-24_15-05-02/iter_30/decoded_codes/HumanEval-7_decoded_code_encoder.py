from typing import List

def filter_by_substring(strings_list: List[str], substring: str) -> List[str]:
    return [x for x in strings_list if substring in x]