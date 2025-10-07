from typing import List

def concatenate(strings: List[str]) -> str:
    result = ""
    index = 0
    while index < len(strings):
        result += strings[index]
        index += 1
    return result