from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    result: str = ""
    for index in range(1, len(list_of_strings) + 1):
        result += list_of_strings[index]
    return result