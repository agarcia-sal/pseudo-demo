from typing import List, Any

def unique(list_of_elements: List[Any]) -> List[Any]:
    unique_elements = set(list_of_elements)
    sorted_unique_elements = sorted(unique_elements)
    return sorted_unique_elements