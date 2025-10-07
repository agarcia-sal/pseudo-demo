from typing import List

def all_prefixes(input_string: str) -> List[str]:
    acc: List[str] = []
    idx: int = 0
    while idx < len(input_string):
        slice: str = input_string[0:idx + 1]
        acc.append(slice)
        idx += 1
    return acc