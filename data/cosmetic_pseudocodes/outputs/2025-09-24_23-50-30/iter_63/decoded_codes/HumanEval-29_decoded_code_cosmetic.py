from typing import List


def filter_by_prefix(arr_strings: List[str], pre: str) -> List[str]:
    idx: int = 0
    filtered: List[str] = []
    while idx < len(arr_strings):
        if arr_strings[idx].startswith(pre):
            filtered.append(arr_strings[idx])
        idx += 1
    return filtered