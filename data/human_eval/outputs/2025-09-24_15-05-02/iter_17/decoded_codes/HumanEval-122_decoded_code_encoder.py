from typing import List, Union

def add_elements(arr: List[Union[int, float]], k: int) -> Union[int, float]:
    total: Union[int, float] = 0
    for elem in arr[:k]:
        if len(str(elem)) <= 2:
            total += elem
    return total