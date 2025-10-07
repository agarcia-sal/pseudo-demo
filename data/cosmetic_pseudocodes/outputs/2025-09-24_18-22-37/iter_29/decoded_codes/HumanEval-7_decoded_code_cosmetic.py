from typing import List

def filter_by_substring(arr_strings: List[str], sub_val: str) -> List[str]:
    filtered_results: List[str] = []
    idx: int = 0
    while idx < len(arr_strings):
        candidate: str = arr_strings[idx]
        if candidate.find(sub_val) != -1:
            filtered_results.append(candidate)
        idx += 1
    return filtered_results