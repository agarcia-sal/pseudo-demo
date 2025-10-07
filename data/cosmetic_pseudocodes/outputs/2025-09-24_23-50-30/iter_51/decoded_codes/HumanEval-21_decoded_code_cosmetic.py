from typing import Sequence, List


def rescale_to_unit(numbers_collection: Sequence[float]) -> List[float]:
    if not numbers_collection:
        return []
    smallest_value: float = min(numbers_collection)
    largest_value: float = max(numbers_collection)
    range_span: float = largest_value - smallest_value
    if range_span == 0:
        return [0.0 for _ in numbers_collection]  # all values equal, normalized to 0

    def normalize_at_index(idx: int) -> float:
        return (numbers_collection[idx] - smallest_value) / range_span

    return [normalize_at_index(i) for i in range(len(numbers_collection))]