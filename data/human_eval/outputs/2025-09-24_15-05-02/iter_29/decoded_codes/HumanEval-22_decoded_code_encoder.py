from typing import List, Any

def filter_integers(list_of_values: List[Any]) -> List[int]:
    return [x for x in list_of_values if isinstance(x, int)]