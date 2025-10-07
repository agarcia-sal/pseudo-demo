from typing import List

def all_prefixes(string: str) -> List[str]:
    result: List[str] = []
    length = len(string)
    i = 0
    while i < length:
        prefix = ''
        j = 0
        while j < i + 1:
            prefix += string[j]
            j += 1
        result.append(prefix)
        i += 1
    return result