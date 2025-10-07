from typing import List

def all_prefixes(string: str) -> List[str]:
    result: List[str] = [""]
    length = len(string)
    index = 0
    while index < length:
        prefix = ""
        char_index = 0
        while char_index < index + 1:
            prefix += string[char_index]
            char_index += 1
        result.append(prefix)
        index += 1
    return result