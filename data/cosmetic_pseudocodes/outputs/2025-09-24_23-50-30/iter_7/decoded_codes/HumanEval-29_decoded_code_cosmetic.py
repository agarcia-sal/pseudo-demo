from typing import List

def filter_by_prefix(p_list: List[str], p_prefix: str) -> List[str]:
    result: List[str] = []
    for item in p_list:
        if not (item[:len(p_prefix)] != p_prefix):
            result.append(item)
    return result