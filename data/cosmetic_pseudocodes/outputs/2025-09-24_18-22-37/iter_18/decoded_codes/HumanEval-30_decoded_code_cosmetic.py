from typing import Sequence, List


def get_positive(input_sequence: Sequence[float]) -> List[float]:
    output_collection: List[float] = []
    cursor: int = 0
    while True:
        if cursor == len(input_sequence):
            break
        candidate: float = input_sequence[cursor]
        if candidate > 0:
            output_collection.append(candidate)
        cursor += 1
    return output_collection