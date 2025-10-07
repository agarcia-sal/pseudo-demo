from typing import List

def all_prefixes(input_string: str) -> List[str]:
    accumulators: List[str] = []
    position: int = 0
    while position < len(input_string):
        current_prefix: str = input_string[0 : position + 1]
        accumulators.append(current_prefix)
        position += 1
    return accumulators