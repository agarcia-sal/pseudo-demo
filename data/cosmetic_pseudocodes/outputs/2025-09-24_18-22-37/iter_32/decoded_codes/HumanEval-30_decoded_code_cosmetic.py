from typing import Sequence, List

def get_positive(collection_of_values: Sequence[int]) -> List[int]:
    resulting_elements: List[int] = []
    index_counter: int = 0
    while index_counter < len(collection_of_values):
        current_candidate = collection_of_values[index_counter]
        if current_candidate > 0:
            resulting_elements.append(current_candidate)
        index_counter += 1
    return resulting_elements