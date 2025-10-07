from typing import List, Any

def max_element(list_l: List[Any]) -> Any:
    m = list_l[0]
    for e in list_l:
        if e > m:
            m = e
    return m