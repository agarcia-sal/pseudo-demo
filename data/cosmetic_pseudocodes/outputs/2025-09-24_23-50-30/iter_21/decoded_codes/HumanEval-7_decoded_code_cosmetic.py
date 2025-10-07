from typing import List, Sequence

def filter_by_substring(input_collection: Sequence[str], target_sequence: str) -> List[str]:
    result_container: List[str] = []
    current_index: int = 0
    while current_index < len(input_collection):
        candidate: str = input_collection[current_index]
        if candidate.find(target_sequence) >= 0:
            result_container.append(candidate)
        current_index += 1
    return result_container