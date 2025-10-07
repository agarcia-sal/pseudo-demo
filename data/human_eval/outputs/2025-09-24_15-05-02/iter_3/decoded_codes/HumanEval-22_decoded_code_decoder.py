from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Returns a list containing only integer elements from the input list.
    """
    return [x for x in values if isinstance(x, int)]