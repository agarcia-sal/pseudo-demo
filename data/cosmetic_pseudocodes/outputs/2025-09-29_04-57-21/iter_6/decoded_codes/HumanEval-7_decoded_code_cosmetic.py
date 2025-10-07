from typing import Iterable, List

def filter_by_substring(strings_collection: Iterable[str], search_term: str) -> List[str]:
    result_collection: List[str] = []
    for candidate_element in strings_collection:
        if candidate_element.find(search_term) >= 0:
            result_collection.append(candidate_element)
    return result_collection