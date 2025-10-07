from typing import Sequence, List

def get_positive(sequence_of_values: Sequence[int]) -> List[int]:
    collection_positive_elements: List[int] = []
    index_counter: int = 0
    index_limit: int = len(sequence_of_values)
    while index_counter < index_limit:
        current_entry: int = sequence_of_values[index_counter]
        if current_entry > 0:
            collection_positive_elements.append(current_entry)
        index_counter += 1
    return collection_positive_elements