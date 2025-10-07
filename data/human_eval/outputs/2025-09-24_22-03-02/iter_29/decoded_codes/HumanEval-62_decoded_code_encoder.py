from typing import List

def derivative(xs: List[int]) -> List[int]:
    result = [()]
    for index in range(len(xs)):
        product = index * xs[index]
        result.append(product)
    result.pop(0)
    return result