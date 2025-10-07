from typing import List

def filter_by_prefix(str_collection: List[str], prefix_param: str) -> List[str]:
    filtered_results: List[str] = []
    idx: int = 0
    while idx < len(str_collection):
        candidate: str = str_collection[idx]
        prefix_len: int = len(prefix_param)
        candidate_prefix: str = candidate[:prefix_len]
        if candidate_prefix == prefix_param:
            filtered_results.append(candidate)
        idx += 1
    return filtered_results