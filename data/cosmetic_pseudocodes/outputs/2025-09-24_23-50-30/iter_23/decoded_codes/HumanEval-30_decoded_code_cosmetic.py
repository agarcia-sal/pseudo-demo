from typing import Iterable, List


def get_positive(collection_of_values: Iterable[float]) -> List[float]:
    return [item for item in collection_of_values if item > 0]