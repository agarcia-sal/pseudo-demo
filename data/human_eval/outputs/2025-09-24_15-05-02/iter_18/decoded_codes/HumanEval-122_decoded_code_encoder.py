from typing import List, Union

def add_elements(arr: List[Union[int, float, str]], k: int) -> Union[int, float]:
    return sum(
        elem for elem in arr[:k]
        if len(str(elem)) <= 2
    )