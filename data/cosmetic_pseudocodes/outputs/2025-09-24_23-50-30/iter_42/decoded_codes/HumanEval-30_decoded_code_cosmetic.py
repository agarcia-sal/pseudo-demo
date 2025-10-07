from typing import Sequence, List

def get_positive(input_sequence: Sequence[int]) -> List[int]:
    result_collection: List[int] = []
    cursor: int = 0
    while cursor < len(input_sequence):
        if input_sequence[cursor] > 0:
            result_collection.append(input_sequence[cursor])
        cursor += 1
    return result_collection