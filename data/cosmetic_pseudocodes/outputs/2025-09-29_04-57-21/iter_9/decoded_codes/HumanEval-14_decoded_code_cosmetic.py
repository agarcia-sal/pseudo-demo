from typing import List

def all_prefixes(input_string: str) -> List[str]:
    collected_prefixes: List[str] = []
    position: int = 0
    while position < len(input_string):
        collected_prefixes.append(input_string[:position + 1])
        position += 1
    return collected_prefixes