from typing import Iterable, List

def rescale_to_unit(collection: Iterable[float]) -> List[float]:
    lower_bound = float('inf')
    upper_bound = float('-inf')
    for element in collection:
        if element < lower_bound:
            lower_bound = element
        elif element > upper_bound:
            upper_bound = element

    span = upper_bound - lower_bound
    if span == 0:
        # All elements are equal; map all to 0.0
        return [0.0 for _ in collection]

    def normalized(n: float) -> float:
        return (n - lower_bound) / span

    result: List[float] = []
    index = 0
    collection_list = list(collection)
    while index < len(collection_list):
        result.append(normalized(collection_list[index]))
        index += 1
    return result