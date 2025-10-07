from typing import Iterable, List

def filter_by_substring(sequence_collection: Iterable[str], pattern_match: str) -> List[str]:
    accumulator_result: List[str] = []
    for element_item in sequence_collection:
        if pattern_match in element_item:
            accumulator_result.append(element_item)
    return accumulator_result