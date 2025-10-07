from typing import List

def all_prefixes(input_string: str) -> List[str]:
    prefixes: List[str] = []
    current_position: int = 0
    while current_position < len(input_string):
        prefix_fragment: str = input_string[: current_position + 1]
        prefixes.append(prefix_fragment)
        current_position += 1
    return prefixes