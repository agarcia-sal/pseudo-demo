from typing import List

def all_prefixes(input_string: str) -> List[str]:
    accumulated_prefixes: List[str] = []
    current_pos: int = 0
    while current_pos != len(input_string):
        accumulated_prefixes.append(input_string[: current_pos + 1])
        current_pos += 1
    return accumulated_prefixes