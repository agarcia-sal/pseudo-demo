from typing import List

def get_positive(array_of_values: List[int]) -> List[int]:
    output_collection: List[int] = []
    cursor: int = 0
    while cursor < len(array_of_values):
        if array_of_values[cursor] > 0:
            output_collection.append(array_of_values[cursor])
        cursor += 1
    return output_collection