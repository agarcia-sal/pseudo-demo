from typing import Sequence, List, Union

def incr_list(collection: Sequence[Union[int, float]]) -> List[Union[int, float]]:
    result: List[Union[int, float]] = []
    idx: int = 0
    while idx < len(collection):
        currentVal = collection[idx]
        incremented = currentVal + 1
        result.append(incremented)
        idx += 1
    return result