from typing import List, Any

def max_element(l: List[Any]) -> Any:
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m