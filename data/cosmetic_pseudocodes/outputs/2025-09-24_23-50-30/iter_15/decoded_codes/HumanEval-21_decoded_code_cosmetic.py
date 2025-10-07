from typing import Sequence, List

def rescale_to_unit(collection_of_values: Sequence[float]) -> List[float]:
    def diff(a: float, b: float) -> float:
        return a - b

    def ratio(a: float, b: float) -> float:
        return a / b

    if not collection_of_values:
        return []

    val_min: float = collection_of_values[0]
    val_max: float = collection_of_values[0]

    index_cursor: int = 1
    length: int = len(collection_of_values)
    while index_cursor < length:
        current = collection_of_values[index_cursor]
        if diff(current, val_max) > 0:
            val_max = current
        if diff(val_min, current) > 0:
            val_min = current
        index_cursor += 1

    denominator = diff(val_max, val_min)
    # Avoid division by zero when all values are equal; return zeros
    if denominator == 0:
        return [0.0 for _ in collection_of_values]

    scaled_list: List[float] = [
        ratio(diff(element, val_min), denominator)
        for element in collection_of_values
    ]
    return scaled_list