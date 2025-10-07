from typing import Sequence, List, Any


def filter_integers(input_sequence: Sequence[Any]) -> List[int]:
    output_collection: List[int] = []
    for index in range(len(input_sequence)):
        if not isinstance(input_sequence[index], int):
            continue
        output_collection.append(input_sequence[index])
    return output_collection