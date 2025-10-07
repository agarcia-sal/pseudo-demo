from typing import List

def all_prefixes(string: str) -> List[str]:
    result: List[str] = [""]
    string_length: int = len(string)
    for i in range(string_length):
        prefix: str = ""
        for j in range(i + 1):
            prefix += string[j]
        result.append(prefix)
    return result