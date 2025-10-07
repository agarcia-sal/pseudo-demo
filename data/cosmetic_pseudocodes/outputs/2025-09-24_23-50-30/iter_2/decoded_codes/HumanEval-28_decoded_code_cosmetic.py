from typing import List


def concatenate(list_of_strings: List[str]) -> str:
    result: str = ""
    index: int = len(list_of_strings) - 1
    while index >= 0:
        result = list_of_strings[index] + result
        index -= 1
    return result