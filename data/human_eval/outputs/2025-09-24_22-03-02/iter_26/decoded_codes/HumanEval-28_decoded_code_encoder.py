from typing import List

def concatenate(strings: List[str]) -> str:
    result = ''
    for index in range(len(strings)):
        current_string = strings[index]
        result += current_string
    return result