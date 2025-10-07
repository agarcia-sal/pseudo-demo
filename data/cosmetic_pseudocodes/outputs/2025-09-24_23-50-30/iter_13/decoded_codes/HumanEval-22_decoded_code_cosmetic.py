from typing import Iterable, List, Union

def filter_integers(input_collection: Iterable[object]) -> List[int]:
    accumulator: List[int] = []
    for candidate_element in input_collection:
        if isinstance(candidate_element, int):
            accumulator.append(candidate_element)
    return accumulator