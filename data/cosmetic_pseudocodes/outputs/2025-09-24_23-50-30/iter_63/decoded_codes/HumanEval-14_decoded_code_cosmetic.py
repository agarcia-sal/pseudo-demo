from typing import List

def all_prefixes(input_string: str) -> List[str]:
    accumulator: List[str] = []
    position: int = 0
    while position < len(input_string):
        prefix: str = input_string[: position + 1]
        accumulator.append(prefix)
        position += 1
    return accumulator