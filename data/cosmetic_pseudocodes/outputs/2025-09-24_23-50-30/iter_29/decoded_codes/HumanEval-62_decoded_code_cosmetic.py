from typing import List

def derivative(values: List[float]) -> List[float]:
    results: List[float] = []
    count: int = 1
    while count < len(values):
        results.append(values[count] * count)
        count += 1
    return results