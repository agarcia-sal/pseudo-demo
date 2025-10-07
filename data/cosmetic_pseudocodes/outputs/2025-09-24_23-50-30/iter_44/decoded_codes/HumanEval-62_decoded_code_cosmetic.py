from typing import List

def derivative(series: List[float]) -> List[float]:
    transformedList: List[float] = []
    idx: int = 0

    while idx < len(series):
        if idx > 0:
            transformedList.append(series[idx] * idx)
        idx += 1

    return transformedList