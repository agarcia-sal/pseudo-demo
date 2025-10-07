from typing import List

def get_positive(array_of_values: List[int]) -> List[int]:
    output_collection: List[int] = []
    index_marker: int = 0

    while index_marker < len(array_of_values):
        candidate: int = array_of_values[index_marker]
        if candidate > 0:
            output_collection.append(candidate)
        index_marker += 1

    return output_collection