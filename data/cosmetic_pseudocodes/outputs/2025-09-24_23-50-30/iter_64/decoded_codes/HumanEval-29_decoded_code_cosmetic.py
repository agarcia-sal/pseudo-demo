from typing import List

def filter_by_prefix(alpha_sequence: List[str], beta_pattern: str) -> List[str]:
    result_collection: List[str] = []
    index_counter: int = 0
    pattern_length: int = len(beta_pattern)
    while index_counter < len(alpha_sequence):
        current_entry: str = alpha_sequence[index_counter]
        if current_entry[:pattern_length] == beta_pattern:
            result_collection.append(current_entry)
        index_counter += 1
    return result_collection