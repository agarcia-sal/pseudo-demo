from typing import Any, List

def filter_integers(list_of_values: List[Any]) -> List[int]:
    return [item for item in list_of_values if isinstance(item, int)]