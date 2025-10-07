from typing import List

def derivative(xs: List[float]) -> List[float]:
    return [index * coefficient for index, coefficient in enumerate(xs) if index > 0]