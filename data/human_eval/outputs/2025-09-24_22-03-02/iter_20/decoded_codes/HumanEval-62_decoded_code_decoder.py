from typing import List

def derivative(xs: List[int]) -> List[int]:
    result = [0]
    for index in range(len(xs)):
        coefficient = xs[index]
        product = index * coefficient
        result.append(product)
    derivative_result = []
    for index in range(1, len(result)):
        element = result[index]
        derivative_result.append(element)
    return derivative_result