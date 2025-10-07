from typing import List

def derivative(xs: List[int]) -> List[int]:
    result = []
    for i in range(len(xs)):
        x = xs[i]
        product = i * x
        result.append(product)
    derivative_result = []
    for element in result[1:]:
        derivative_result.append(element)
    return derivative_result