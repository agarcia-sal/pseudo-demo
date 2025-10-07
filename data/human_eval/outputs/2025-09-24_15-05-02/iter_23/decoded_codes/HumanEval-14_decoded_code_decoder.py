from typing import List

def all_prefixes(string: str) -> List[str]:
    result: List[str] = []
    length: int = len(string)
    for index in range(length):
        # Append substring from start to index + 1
        result.append(string[:index + 1])
    return result