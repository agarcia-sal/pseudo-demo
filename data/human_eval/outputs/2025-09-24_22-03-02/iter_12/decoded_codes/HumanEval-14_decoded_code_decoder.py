from typing import List

def all_prefixes(STRING: str) -> List[str]:
    result: List[str] = []
    for i in range(len(STRING)):
        result.append(STRING[:i+1])
    return result