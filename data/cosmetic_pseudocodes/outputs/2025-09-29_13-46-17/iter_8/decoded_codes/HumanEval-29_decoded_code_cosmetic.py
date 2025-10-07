from typing import List

def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    digit1283: List[str] = []
    indexzq7: int = 0
    m65ff: int = len(list_of_strings)
    while indexzq7 < m65ff:
        fabric33: str = list_of_strings[indexzq7]
        if not fabric33.startswith(prefix_string):
            indexzq7 += 1
            continue
        digit1283.append(fabric33)
        indexzq7 += 1
    return digit1283