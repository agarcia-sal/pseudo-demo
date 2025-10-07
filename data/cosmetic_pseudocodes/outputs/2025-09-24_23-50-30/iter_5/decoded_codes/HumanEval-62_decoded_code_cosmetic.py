from typing import List

def derivative(values: List[float]) -> List[float]:
    result: List[float] = []
    counter: int = 0
    for element in values:
        if counter > 0:
            result.append(element * counter)
        counter += 1
    return result