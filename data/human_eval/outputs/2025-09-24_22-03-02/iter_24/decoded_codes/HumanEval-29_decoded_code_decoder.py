from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    result = []
    index = 0
    while index < len(strings):
        x = strings[index]
        if x.startswith(prefix) == True:
            result.append(x)
        index += 1
    return result