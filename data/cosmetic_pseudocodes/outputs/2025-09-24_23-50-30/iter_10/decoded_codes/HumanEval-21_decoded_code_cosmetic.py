from typing import Sequence, List

def rescale_to_unit(collection: Sequence[float]) -> List[float]:
    if not collection:
        return []
    smallest: float = collection[0]
    largest: float = collection[0]

    for element in collection:
        if element < smallest:
            smallest = element
        if element > largest:
            largest = element

    scale_factor: float = largest - smallest
    if scale_factor == 0:
        # All elements are equal; return zeros
        return [0.0] * len(collection)

    adjusted_list: List[float] = [(item - smallest) / scale_factor for item in collection]
    return adjusted_list