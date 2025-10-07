from typing import List

def all_prefixes(input_string: str) -> List[str]:
    prefixes: List[str] = []
    position: int = 0
    while position < len(input_string):
        prefixes.append(input_string[:position + 1])
        position += 1
    return prefixes