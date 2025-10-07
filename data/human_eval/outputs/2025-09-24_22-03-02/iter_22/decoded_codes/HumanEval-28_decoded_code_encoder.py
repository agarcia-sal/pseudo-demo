from typing import List

def concatenate(strings: List[str]) -> str:
    result = ''
    for index in range(len(strings)):
        result += strings[index]
    return result