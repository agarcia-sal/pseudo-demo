from typing import Iterable, List

def get_positive(inputs: Iterable[float]) -> List[float]:
    return [item for item in inputs if item > 0]