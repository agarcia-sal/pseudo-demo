from typing import List

def derivative(xs: List[int]) -> List[int]:
    return [index * element for index, element in enumerate(xs)][1:]