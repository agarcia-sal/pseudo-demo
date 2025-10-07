from typing import List

def derivative(xs: List[int]) -> List[int]:
    result = []
    length = len(xs)
    i = 0
    while i < length:
        x = xs[i]
        product = i * x
        result.append(product)
        i += 1
    derivative_result = []
    j = 1
    result_length = len(result)
    while j < result_length:
        element = result[j]
        derivative_result.append(element)
        j += 1
    return derivative_result