from typing import Iterable, List

def filter_by_substring(source_collection: Iterable[str], pattern_value: str) -> List[str]:
    collected_results: List[str] = []
    for candidate_element in source_collection:
        if candidate_element.find(pattern_value) != -1:
            collected_results.append(candidate_element)
    return collected_results