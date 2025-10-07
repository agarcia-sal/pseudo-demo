from typing import List

def all_prefixes(input_string: str) -> List[str]:
    prefixes: List[str] = []
    i: int = 0
    while i < len(input_string):
        prefixes.append(input_string[0 : i + 1])
        i += 1
    return prefixes