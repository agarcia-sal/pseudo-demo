from typing import Any, List

def filter_integers(array_of_items: List[Any]) -> List[int]:
    return [item for item in array_of_items if isinstance(item, int)]