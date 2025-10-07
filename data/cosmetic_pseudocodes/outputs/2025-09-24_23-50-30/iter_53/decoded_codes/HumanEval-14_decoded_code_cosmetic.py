from typing import List

def all_prefixes(param_data: str) -> List[str]:
    accumulator: List[str] = []
    position: int = 0
    while position < len(param_data):
        accumulator.append(param_data[:position + 1])
        position += 1
    return accumulator