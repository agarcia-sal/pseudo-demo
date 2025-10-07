from typing import List, Any

def max_element(l: List[Any]) -> Any:
    m = l[0]
    for index in range(len(l)):
        e = l[index]
        if e > m:
            m = e
    return m