from typing import List

def all_prefixes(input_string: str) -> List[str]:
    accumulation: List[str] = []
    cursor: int = 0
    while cursor < len(input_string):
        prefix_end: int = cursor + 1
        segment: str = input_string[0:prefix_end]
        accumulation.append(segment)
        cursor += 1
    return accumulation