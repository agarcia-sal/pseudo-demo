from typing import List


def all_prefixes(input_string: str) -> List[str]:
    collected_prefixes: List[str] = []
    position_tracker: int = 0
    while position_tracker < len(input_string):
        upper_bound: int = position_tracker + 1
        prefix_segment: str = input_string[0:upper_bound]
        collected_prefixes.append(prefix_segment)
        position_tracker += 1
    return collected_prefixes