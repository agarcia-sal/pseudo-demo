from typing import List

def all_prefixes(alph_str: str) -> List[str]:
    idx: int = 0
    accum: List[str] = []
    while idx < len(alph_str):
        accum.append(alph_str[: idx + 1])
        idx += 1
    return accum