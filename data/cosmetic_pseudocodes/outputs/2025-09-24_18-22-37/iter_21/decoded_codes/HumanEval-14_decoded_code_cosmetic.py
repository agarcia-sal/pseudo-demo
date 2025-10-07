from typing import List

def all_prefixes(input_string_param: str) -> List[str]:
    accumulated_prefixes: List[str] = []
    current_index: int = 0
    while current_index <= len(input_string_param) - 1:
        substring_limit: int = current_index + 1
        prefix_piece: str = input_string_param[:substring_limit]
        accumulated_prefixes.append(prefix_piece)
        current_index += 1
    return accumulated_prefixes