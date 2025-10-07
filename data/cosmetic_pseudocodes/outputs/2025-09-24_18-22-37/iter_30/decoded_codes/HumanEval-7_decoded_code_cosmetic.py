from typing import List

def filter_by_substring(collection_of_texts: List[str], query_fragment: str) -> List[str]:
    result_list: List[str] = []
    idx: int = 0
    while idx < len(collection_of_texts):
        current_element: str = collection_of_texts[idx]
        contains_fragment: bool = query_fragment in current_element
        if contains_fragment:
            result_list.append(current_element)
        idx += 1
    return result_list