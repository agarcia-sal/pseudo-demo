from typing import List

def all_prefixes(input_string: str) -> List[str]:
    prefixes: List[str] = []
    position: int = 0
    while position < len(input_string):
        current_prefix: str = input_string[:position + 1]
        prefixes.append(current_prefix)
        position += 1
    return prefixes