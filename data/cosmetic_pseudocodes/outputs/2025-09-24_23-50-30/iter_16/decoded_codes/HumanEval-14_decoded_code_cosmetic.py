from typing import List


def all_prefixes(input_string: str) -> List[str]:
    accumulated_prefixes: List[str] = []
    current_position: int = 0
    while current_position != len(input_string):
        prefix_segment = input_string[: current_position + 1]
        accumulated_prefixes.append(prefix_segment)
        current_position += 1
    return accumulated_prefixes