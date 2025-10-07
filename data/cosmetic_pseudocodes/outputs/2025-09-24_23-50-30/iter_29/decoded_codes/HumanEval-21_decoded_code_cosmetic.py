from typing import Sequence, List

def rescale_to_unit(collection: Sequence[float]) -> List[float]:
    if not collection:
        return []
    lower_bound = upper_bound = collection[0]
    for element in collection:
        if element < lower_bound:
            lower_bound = element
        elif element > upper_bound:
            upper_bound = element
    range_span = upper_bound - lower_bound
    if range_span == 0:
        return [0.0 for _ in collection]
    return [(value - lower_bound) / range_span for value in collection]