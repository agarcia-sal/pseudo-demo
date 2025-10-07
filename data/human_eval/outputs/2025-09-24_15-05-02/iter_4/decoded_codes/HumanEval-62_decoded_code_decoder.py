from typing import List

def derivative(xs: List[int]) -> List[int]:
    return [index * coefficient for index, coefficient in enumerate(xs[1:], start=1)]