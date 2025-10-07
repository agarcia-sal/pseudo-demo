from typing import List

def all_prefixes(string: str) -> List[str]:
    return [string[:index + 1] for index in range(len(string))]