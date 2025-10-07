from typing import List, Any

def max_element(l: List[Any]) -> Any:
    if not l:
        raise ValueError("max_element() arg is an empty list")
    m = l[0]
    for i in range(len(l)):
        e = l[i]
        if e > m:
            m = e
    return m