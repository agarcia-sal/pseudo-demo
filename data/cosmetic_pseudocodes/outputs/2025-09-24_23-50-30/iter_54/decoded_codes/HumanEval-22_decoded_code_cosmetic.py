from typing import Sequence, List, Any

def filter_integers(input_sequence: Sequence[Any]) -> List[int]:
    output_collection: List[int] = []
    for idx in range(len(input_sequence)):
        candidate = input_sequence[idx]
        if isinstance(candidate, int):
            output_collection.append(candidate)
    return output_collection