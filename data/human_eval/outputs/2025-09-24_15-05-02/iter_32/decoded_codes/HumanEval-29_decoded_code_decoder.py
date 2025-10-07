from typing import List

def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    return [each_string for each_string in list_of_strings if each_string.startswith(prefix_string)]