from bisect import insort
from typing import List, Union

def median(arr: List[float]) -> float:
    sortedArr: List[float] = []
    for idx in range(len(arr)):
        insort(sortedArr, arr[idx])

    count = len(sortedArr)
    if count % 2 != 0:
        return float(sortedArr[count // 2])
    else:
        mid = count // 2
        return (sortedArr[mid - 1] + sortedArr[mid]) / 2.0