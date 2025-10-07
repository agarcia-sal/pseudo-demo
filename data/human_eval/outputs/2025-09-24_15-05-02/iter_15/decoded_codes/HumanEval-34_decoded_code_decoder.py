from typing import List, Any

def unique(list_l: List[Any]) -> List[Any]:
    unique_elements = set(list_l)
    unique_list = list(unique_elements)
    sorted_unique_list = sorted(unique_list)
    return sorted_unique_list