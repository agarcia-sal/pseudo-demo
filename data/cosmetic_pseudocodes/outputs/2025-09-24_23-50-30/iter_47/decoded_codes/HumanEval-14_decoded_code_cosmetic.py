from typing import List


def all_prefixes(input_string: str) -> List[str]:
    collected_prefixes: List[str] = []
    current_index: int = 0
    while current_index <= len(input_string) - 1:
        start_pos: int = 0
        end_pos: int = current_index + 1
        prefix_fragment: str = input_string[start_pos:end_pos]
        collected_prefixes.append(prefix_fragment)
        current_index += 1
    return collected_prefixes