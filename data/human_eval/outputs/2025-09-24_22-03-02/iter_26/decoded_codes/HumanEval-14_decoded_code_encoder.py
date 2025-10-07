from typing import List

def all_prefixes(string: str) -> List[str]:
    result = [""]
    length_of_string = len(string)
    for i in range(length_of_string):
        prefix = ""
        for j in range(i + 1):
            prefix += string[j]
        result.append(prefix)
    return result