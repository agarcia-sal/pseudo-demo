from typing import List


def all_prefixes(string: str) -> List[str]:
    result: List[str] = []
    for index in range(len(string)):
        result.append(string[:index+1])
    return result