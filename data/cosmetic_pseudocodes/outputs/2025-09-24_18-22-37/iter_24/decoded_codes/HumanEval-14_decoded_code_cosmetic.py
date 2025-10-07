from typing import List

def all_prefixes(input_string: str) -> List[str]:
    collected_prefixes: List[str] = []
    current_position: int = 0
    while current_position < len(input_string):
        partial_prefix: str = input_string[: current_position + 1]
        collected_prefixes.append(partial_prefix)
        current_position += 1
    return collected_prefixes