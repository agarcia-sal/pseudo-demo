from typing import List

def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    return [candidate_string for candidate_string in list_of_strings if candidate_string.startswith(prefix_string)]