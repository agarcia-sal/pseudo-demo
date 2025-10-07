from typing import Sequence, List, Union

def filter_integers(input_sequence: Sequence[object]) -> List[int]:
    result_collection: List[int] = []
    for index in range(len(input_sequence)):
        candidate = input_sequence[index]
        if type(candidate) is int:
            result_collection.append(candidate)
    return result_collection