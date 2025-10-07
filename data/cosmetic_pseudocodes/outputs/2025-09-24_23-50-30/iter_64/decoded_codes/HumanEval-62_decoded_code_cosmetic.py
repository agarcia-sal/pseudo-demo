from typing import List

def derivative(arr: List[float]) -> List[float]:
    idx: int = 1
    resultList: List[float] = []
    while idx < len(arr):
        val: float = arr[idx]
        newVal: float = val * idx
        resultList.append(newVal)
        idx += 1
    return resultList