from typing import List

def all_prefixes(parameter_s: str) -> List[str]:
    accumulation: List[str] = []
    cursor: int = 0
    while cursor < len(parameter_s):
        accumulation.append(parameter_s[:cursor + 1])
        cursor += 1
    return accumulation