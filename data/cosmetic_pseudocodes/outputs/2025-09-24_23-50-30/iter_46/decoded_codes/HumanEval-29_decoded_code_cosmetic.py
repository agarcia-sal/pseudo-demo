from typing import List

def filter_by_prefix(collection_var: List[str], key_var: str) -> List[str]:
    def recursive_filter(curr_index: int, result_accum: List[str]) -> List[str]:
        if curr_index >= len(collection_var):
            return result_accum
        element_var = collection_var[curr_index]
        if element_var.startswith(key_var):
            return recursive_filter(curr_index + 1, result_accum + [element_var])
        return recursive_filter(curr_index + 1, result_accum)
    return recursive_filter(0, [])