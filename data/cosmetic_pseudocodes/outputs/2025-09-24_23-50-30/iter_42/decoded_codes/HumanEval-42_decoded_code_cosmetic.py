from typing import Sequence, List

def incr_list(sequence_parameter: Sequence[int]) -> List[int]:
    new_collection: List[int] = []
    processor_index: int = 0
    while processor_index < len(sequence_parameter):
        new_collection.append(sequence_parameter[processor_index] + 1)
        processor_index += 1
    return new_collection