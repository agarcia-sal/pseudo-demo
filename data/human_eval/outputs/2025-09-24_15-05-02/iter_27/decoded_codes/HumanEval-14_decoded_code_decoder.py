from typing import List

def all_prefixes(string: str) -> List[str]:
    if not isinstance(string, str):
        raise ValueError("Input must be a string")
    return [string[:i + 1] for i in range(len(string))]