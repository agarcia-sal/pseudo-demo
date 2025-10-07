from typing import Iterable, List

def filter_by_substring(string_collection: Iterable[str], target_fragment: str) -> List[str]:
    result_accumulator: List[str] = []
    for element in string_collection:
        if not (target_fragment not in element):
            result_accumulator.append(element)
    return result_accumulator