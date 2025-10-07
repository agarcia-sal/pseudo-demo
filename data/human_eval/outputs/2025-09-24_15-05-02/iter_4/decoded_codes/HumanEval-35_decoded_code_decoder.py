from typing import List, Any

def max_element(l: List[Any]) -> Any:
    if not l:
        raise ValueError("max_element() arg is an empty list")
    max_value = l[0]
    for element in l:
        if element > max_value:
            max_value = element
    return max_value