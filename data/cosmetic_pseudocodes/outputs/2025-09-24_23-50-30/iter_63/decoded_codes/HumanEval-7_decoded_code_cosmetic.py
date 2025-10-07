from typing import Iterable, List

def filter_by_substring(collection_alpha: Iterable[str], key_beta: str) -> List[str]:
    accumulator_gamma: List[str] = []
    for element_delta in collection_alpha:
        if key_beta in element_delta:
            accumulator_gamma.append(element_delta)
    return accumulator_gamma