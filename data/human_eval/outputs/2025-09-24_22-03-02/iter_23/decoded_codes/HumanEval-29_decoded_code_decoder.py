from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    result: List[str] = []
    for index in range(len(strings)):
        x = strings[index]
        if x.startswith(prefix) == True:
            result.append(x)
    return result