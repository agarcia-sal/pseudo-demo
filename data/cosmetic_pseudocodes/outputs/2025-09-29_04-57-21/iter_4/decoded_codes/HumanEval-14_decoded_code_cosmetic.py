from typing import List

def all_prefixes(input_string: str) -> List[str]:
    result: List[str] = []
    position: int = 0
    while position < len(input_string):
        prefix_segment: str = input_string[:position + 1]
        result.append(prefix_segment)
        position += 1
    return result