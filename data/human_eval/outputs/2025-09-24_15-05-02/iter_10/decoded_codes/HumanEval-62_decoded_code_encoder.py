from typing import List

def derivative(xs: List[float]) -> List[float]:
    result = []
    for index in range(len(xs)):
        coefficient = xs[index]
        product = index * coefficient
        result.append(product)
    if result:
        result.pop(0)
    return result