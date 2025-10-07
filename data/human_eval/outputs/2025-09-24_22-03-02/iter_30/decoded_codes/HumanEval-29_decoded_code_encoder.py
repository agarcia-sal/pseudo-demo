from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    result = []
    for index in range(len(strings)):
        x = strings[index]
        if x.startswith(prefix):
            result.append(x)
    return result