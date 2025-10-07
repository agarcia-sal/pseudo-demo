from typing import List

def concatenate(strings: List[str]) -> str:
    result = ""
    index = 0
    while index < len(strings):
        current_string = strings[index]
        result += current_string
        index += 1
    return result