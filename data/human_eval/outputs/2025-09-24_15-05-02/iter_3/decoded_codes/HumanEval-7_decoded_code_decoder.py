from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Returns a list of strings from the input list that contain the given substring.
    """
    return [s for s in strings if substring in s]