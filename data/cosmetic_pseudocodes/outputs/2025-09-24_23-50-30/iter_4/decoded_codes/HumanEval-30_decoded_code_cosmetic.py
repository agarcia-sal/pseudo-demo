from typing import Iterable, List

def get_positive(numbers: Iterable[float]) -> List[float]:
    return [n for n in numbers if n > 0]