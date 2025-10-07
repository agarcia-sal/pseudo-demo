from typing import List

def derivative(xs: List[int]) -> List[int]:
    result = [0]
    for index in range(len(xs) - 1):
        coefficient = xs[index]
        product = index * coefficient
        result.append(product)
    sliced_result = [0]
    for index in range(1, len(result) - 1):
        element = result[index]
        sliced_result.append(element)
    return sliced_result