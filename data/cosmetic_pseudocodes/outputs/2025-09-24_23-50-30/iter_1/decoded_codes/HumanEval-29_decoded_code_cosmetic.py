from typing import List


def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    return [item for item in list_of_strings if item.startswith(prefix_string)]