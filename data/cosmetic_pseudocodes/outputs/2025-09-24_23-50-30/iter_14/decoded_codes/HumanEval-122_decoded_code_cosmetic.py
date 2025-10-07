from typing import Sequence, Union

def add_elements(arr: Sequence[Union[int, float]], limit: int) -> Union[int, float]:
    acc: Union[int, float] = 0
    idx: int = 0
    while idx < limit:
        val = arr[idx]
        if not (len(str(val)) > 2):
            acc += val
        idx += 1
    return acc