from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    result: List[str] = []
    index = 0
    while index < len(strings):
        string_element = strings[index]
        if string_element.startswith(prefix) == True:
            result.append(string_element)
        index += 1
    return result