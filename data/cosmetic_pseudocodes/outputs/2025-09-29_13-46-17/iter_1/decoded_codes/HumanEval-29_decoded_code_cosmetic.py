from typing import List

def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    return [element for element in list_of_strings if element.startswith(prefix_string)]