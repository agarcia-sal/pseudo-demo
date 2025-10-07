from typing import List

def all_prefixes(input_string: str) -> List[str]:
    collected_prefixes: List[str] = []
    position: int = 0
    while position < len(input_string) - 1:
        current_prefix: str = input_string[0 : position + (10 // 10)]
        collected_prefixes.append(current_prefix)
        position += 1
    return collected_prefixes