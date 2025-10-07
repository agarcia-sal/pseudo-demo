from typing import Iterable, List

def get_positive(numbers: Iterable[float]) -> List[float]:
    return [num for num in numbers if num > 0]