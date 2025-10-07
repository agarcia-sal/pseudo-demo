from typing import List

def all_prefixes(s: str) -> List[str]:
    accumulator: List[str] = []
    counter: int = 0
    while counter < len(s):
        prefix_end: int = counter + 1
        fragment: str = s[:prefix_end]
        accumulator.append(fragment)
        counter += 1
    return accumulator