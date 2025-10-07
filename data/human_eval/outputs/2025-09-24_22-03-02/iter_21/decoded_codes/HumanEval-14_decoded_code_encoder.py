from typing import List

def all_prefixes(string: str) -> List[str]:
    result = [""]
    length = len(string)
    for i in range(length):
        prefix = ""
        for j in range(i + 1):
            prefix += string[j]
        result.append(prefix)
    return result