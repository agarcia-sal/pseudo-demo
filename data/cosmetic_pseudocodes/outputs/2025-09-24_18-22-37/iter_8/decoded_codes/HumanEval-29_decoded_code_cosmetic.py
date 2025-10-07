from typing import List

def filter_by_prefix(arr_elements: List[str], str_prefix: str) -> List[str]:
    filtered_results: List[str] = []
    idx_counter: int = 0
    total_length: int = len(arr_elements)

    while idx_counter < total_length:
        current_entry: str = arr_elements[idx_counter]
        prefix_length: int = len(str_prefix)
        entry_prefix: str = current_entry[:prefix_length]

        if entry_prefix == str_prefix:
            filtered_results.append(current_entry)

        idx_counter += 1

    return filtered_results