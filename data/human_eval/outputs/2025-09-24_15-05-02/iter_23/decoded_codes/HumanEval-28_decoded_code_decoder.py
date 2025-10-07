from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    if not all(isinstance(s, str) for s in list_of_strings):
        raise TypeError("All elements of list_of_strings must be strings")
    return "".join(list_of_strings)