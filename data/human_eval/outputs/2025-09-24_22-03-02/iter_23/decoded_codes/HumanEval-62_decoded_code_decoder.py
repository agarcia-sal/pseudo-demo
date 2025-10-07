from typing import List

def derivative(xs: List[int]) -> List[int]:
    result = [0]
    for index in range(len(xs)):
        x = xs[index]
        product = index * x
        result.append(product)
    derivative_result = [0]
    for index in range(1, len(result)):
        value = result[index]
        derivative_result.append(value)
    return derivative_result