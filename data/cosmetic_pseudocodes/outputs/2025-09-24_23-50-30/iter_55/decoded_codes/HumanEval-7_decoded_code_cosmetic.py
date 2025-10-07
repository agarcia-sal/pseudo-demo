from typing import List

def filter_by_substring(collection_param: List[str], text_param: str) -> List[str]:
    result_storage: List[str] = []
    iterator_var: int = 0
    while iterator_var < len(collection_param):
        if text_param in collection_param[iterator_var]:
            result_storage.append(collection_param[iterator_var])
        iterator_var += 1
    return result_storage