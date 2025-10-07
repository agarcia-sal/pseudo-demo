from typing import List, Any

def max_element(l: List[Any]) -> Any:
    if not l:
        raise ValueError("max_element() arg is an empty list")
    m = l[0]
    i = 0
    while i < len(l):
        e = l[i]
        if e > m:
            m = e
        i += 1
    return m