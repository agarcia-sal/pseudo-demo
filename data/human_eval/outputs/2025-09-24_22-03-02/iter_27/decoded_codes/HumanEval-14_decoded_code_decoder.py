from typing import List

def all_prefixes(string: str) -> List[str]:
    result = [""]
    length = len(string)
    for index in range(length):
        prefix = ""
        for subindex in range(index + 1):
            prefix += string[subindex]
        result.append(prefix)
    return result