from typing import List

def concatenate(strings: List[str]) -> str:
    result = ""
    i = 0
    while i < len(strings):
        result += strings[i]
        i += 1
    return result