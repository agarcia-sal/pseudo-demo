from typing import List

def concatenate(strings: List[str]) -> str:
    result = ""
    index = 0
    while index < len(strings):
        element = strings[index]
        result += element
        index += 1
    return result