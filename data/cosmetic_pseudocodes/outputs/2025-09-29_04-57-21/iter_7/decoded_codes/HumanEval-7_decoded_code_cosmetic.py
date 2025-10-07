from typing import Sequence, List

def filter_by_substring(collection: Sequence[str], subtext: str) -> List[str]:
    result_list: List[str] = []
    idx: int = 1
    while idx <= len(collection):
        current_item = collection[idx - 1]  # Adjust for zero-based indexing
        if not (subtext not in current_item):
            result_list.append(current_item)
        idx += 1
    return result_list