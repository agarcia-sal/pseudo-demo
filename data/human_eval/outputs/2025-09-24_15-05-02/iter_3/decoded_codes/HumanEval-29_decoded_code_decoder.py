from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filters and returns strings that start with the given prefix.

    :param strings: List of strings to filter.
    :param prefix: The prefix to filter strings by.
    :return: List of strings starting with the prefix.
    """
    return [s for s in strings if s.startswith(prefix)]