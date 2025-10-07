from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    if not list_of_strings:
        return ""
    head, tail = list_of_strings[0], list_of_strings[1:]
    return head + concatenate(tail)