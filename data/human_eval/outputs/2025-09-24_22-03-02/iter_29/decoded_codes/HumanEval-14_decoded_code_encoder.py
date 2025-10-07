from typing import List

def all_prefixes(string: str) -> List[str]:
    result = [""]
    for i in range(len(string)):
        prefix = ""
        for j in range(i + 1):
            prefix += string[j]
        result.append(prefix)
    return result