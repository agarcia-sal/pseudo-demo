from typing import List

def all_prefixes(str_param: str) -> List[str]:
    prefixes: List[str] = []
    idx: int = 0
    while idx < len(str_param):
        part: str = str_param[:idx + 1]
        prefixes.append(part)
        idx += 1
    return prefixes