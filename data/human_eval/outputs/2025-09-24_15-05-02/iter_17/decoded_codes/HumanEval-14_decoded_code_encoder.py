from typing import List

def all_prefixes(string: str) -> List[str]:
    result: List[str] = []
    for i in range(len(string)):
        result.append(string[:i + 1])
    return result