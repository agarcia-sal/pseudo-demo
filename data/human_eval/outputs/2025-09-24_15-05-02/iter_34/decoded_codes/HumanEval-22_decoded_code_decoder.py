from typing import List, Any


def filter_integers(list_of_values: List[Any]) -> List[int]:
    return [element for element in list_of_values if isinstance(element, int)]