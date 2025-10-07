from typing import List

def filter_by_substring(source_list: List[str], key_fragment: str) -> List[str]:
    result_collector: List[str] = []
    for candidate_element in source_list:
        if not (key_fragment not in candidate_element):
            result_collector.append(candidate_element)
    return result_collector